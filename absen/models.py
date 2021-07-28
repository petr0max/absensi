from absen import db

# For models database
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)
    authenticated = db.Column(db.Boolean, default=False)


    def __init__(self, email, password_plaintext):
        self.email = email
        self.password_hash = password_plaintext
        self.authenticated = False

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def set_password(self, password_plaintext):
        self.password_hash = bcrypt.generate_password_hash(password_plaintext)

    
    def is_correct_password(self, password_plaintext):
        return bcrypt.check_password_hash(self.password_hash, password_plaintext)

    @property
    def is_authenticated(self):
        return self.authenticated

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    
    # Function get ID
    def get_id(self):
        return str(self.id)


    # Database representation
    def __repr__(self):
        return f"<User {self.email}"
