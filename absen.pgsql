--
-- PostgreSQL database dump
--

-- Dumped from database version 12.7
-- Dumped by pg_dump version 12.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: absens; Type: TABLE; Schema: public; Owner: petro
--

CREATE TABLE public.absens (
    id integer NOT NULL,
    dates date,
    jam_datang time without time zone,
    jam_pulang time without time zone,
    keterangan character varying(64),
    member_id integer
);


ALTER TABLE public.absens OWNER TO petro;

--
-- Name: absens_id_seq; Type: SEQUENCE; Schema: public; Owner: petro
--

CREATE SEQUENCE public.absens_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.absens_id_seq OWNER TO petro;

--
-- Name: absens_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: petro
--

ALTER SEQUENCE public.absens_id_seq OWNED BY public.absens.id;


--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: petro
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO petro;

--
-- Name: permits; Type: TABLE; Schema: public; Owner: petro
--

CREATE TABLE public.permits (
    id integer NOT NULL,
    long_date integer,
    start_date date,
    keterangan character varying(64),
    disetujui boolean,
    member_id integer
);


ALTER TABLE public.permits OWNER TO petro;

--
-- Name: permits_id_seq; Type: SEQUENCE; Schema: public; Owner: petro
--

CREATE SEQUENCE public.permits_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.permits_id_seq OWNER TO petro;

--
-- Name: permits_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: petro
--

ALTER SEQUENCE public.permits_id_seq OWNED BY public.permits.id;


--
-- Name: profiles; Type: TABLE; Schema: public; Owner: petro
--

CREATE TABLE public.profiles (
    id integer NOT NULL,
    realname character varying(64),
    location character varying(64),
    about_me text,
    study character varying(64),
    jurusan character varying(64),
    gelar character varying(64),
    address_before character varying(64),
    address_now character varying(64),
    blood character varying(64),
    religion character varying(64),
    warga_negara character varying(64),
    nik integer,
    npwp integer,
    no_hp integer,
    zone character varying(64),
    member_id integer,
    gender character varying(64),
    married character varying(64),
    birthday date
);


ALTER TABLE public.profiles OWNER TO petro;

--
-- Name: profiles_id_seq; Type: SEQUENCE; Schema: public; Owner: petro
--

CREATE SEQUENCE public.profiles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.profiles_id_seq OWNER TO petro;

--
-- Name: profiles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: petro
--

ALTER SEQUENCE public.profiles_id_seq OWNED BY public.profiles.id;


--
-- Name: roles; Type: TABLE; Schema: public; Owner: petro
--

CREATE TABLE public.roles (
    id integer NOT NULL,
    name character varying(64),
    "default" boolean,
    permissions integer
);


ALTER TABLE public.roles OWNER TO petro;

--
-- Name: roles_id_seq; Type: SEQUENCE; Schema: public; Owner: petro
--

CREATE SEQUENCE public.roles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.roles_id_seq OWNER TO petro;

--
-- Name: roles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: petro
--

ALTER SEQUENCE public.roles_id_seq OWNED BY public.roles.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: petro
--

CREATE TABLE public.users (
    id integer NOT NULL,
    email character varying(64),
    username character varying(64),
    role_id integer,
    confirmed boolean,
    member_since date,
    last_seen timestamp without time zone,
    password character varying(128)
);


ALTER TABLE public.users OWNER TO petro;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: petro
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO petro;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: petro
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: absens id; Type: DEFAULT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.absens ALTER COLUMN id SET DEFAULT nextval('public.absens_id_seq'::regclass);


--
-- Name: permits id; Type: DEFAULT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.permits ALTER COLUMN id SET DEFAULT nextval('public.permits_id_seq'::regclass);


--
-- Name: profiles id; Type: DEFAULT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.profiles ALTER COLUMN id SET DEFAULT nextval('public.profiles_id_seq'::regclass);


--
-- Name: roles id; Type: DEFAULT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.roles ALTER COLUMN id SET DEFAULT nextval('public.roles_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: absens; Type: TABLE DATA; Schema: public; Owner: petro
--

COPY public.absens (id, dates, jam_datang, jam_pulang, keterangan, member_id) FROM stdin;
2	2021-08-25	07:53:00	16:00:00	semua run absen menu	1
1	2021-08-26	08:28:00	15:15:00	pengerjaan halamn admin	1
3	2021-08-26	15:17:00	\N	\N	5
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: petro
--

COPY public.alembic_version (version_num) FROM stdin;
88d53ba7343e
\.


--
-- Data for Name: permits; Type: TABLE DATA; Schema: public; Owner: petro
--

COPY public.permits (id, long_date, start_date, keterangan, disetujui, member_id) FROM stdin;
2	3	2021-08-25	Jenguk ibu	f	1
3	12	2021-08-24	izin ke jawa	f	1
\.


--
-- Data for Name: profiles; Type: TABLE DATA; Schema: public; Owner: petro
--

COPY public.profiles (id, realname, location, about_me, study, jurusan, gelar, address_before, address_now, blood, religion, warga_negara, nik, npwp, no_hp, zone, member_id, gender, married, birthday) FROM stdin;
9	MARDIN WIJAYA	\N		\N	\N	\N	\N	\N	A	\N	WNI	\N	\N	\N	WIB	28	Pria	Menikah	\N
5	john aja								A		WNI	\N	\N	\N	WIB	1	Pria	Menikah	\N
\.


--
-- Data for Name: roles; Type: TABLE DATA; Schema: public; Owner: petro
--

COPY public.roles (id, name, "default", permissions) FROM stdin;
3	User	t	7
2	Moderator	f	15
1	Admin	f	31
4	Owner	f	63
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: petro
--

COPY public.users (id, email, username, role_id, confirmed, member_since, last_seen, password) FROM stdin;
2	david@example.com	david	4	t	\N	\N	$2a$10$t/sbBm0q0KvoFm2YUHMWteDLyBakryQ0h4A8cCyI1azfDAhcuju/e
28	mardinw26@gmail.com	mardin	3	t	2021-08-23	2021-08-23 16:12:19	$2a$10$6D1YKSUTT2oW8F6KSjMfxuGXpQXNIAh3/Zquoo8EYh32k/cxmj/JG
1	john@example.com	john	1	t	2021-08-23	2021-08-27 12:57:12.680561	$2a$10$mqNoYHRSMCwdx4Xxin8vIuwdqjzVzpBWxeqJpQ0t2PNxDV14lRghq
5	ujang@example.com	ujang	2	t	\N	2021-08-27 08:51:42.487428	$2a$10$llEQQCIjZqy7P1rZPSGuZeVpYsPtIgR0kVYmYHkAp2TV2d/4xIXPC
27	susan@example.com	susan	3	t	2021-08-19	2021-08-26 11:25:21.515718	$2a$10$E3xLAjzGDb2lmn6EyLtJg.OOai7etzux.dinFnDqkzApwN/pJsLRS
29	joni@example.com	joni	3	f	2021-08-27	2021-08-27 11:28:08.333781	$2a$10$UEq7d4564JEjTcP3s7xxiuIu97mzdtcpZBxNnitGHhRvLQx2w0u3G
\.


--
-- Name: absens_id_seq; Type: SEQUENCE SET; Schema: public; Owner: petro
--

SELECT pg_catalog.setval('public.absens_id_seq', 3, true);


--
-- Name: permits_id_seq; Type: SEQUENCE SET; Schema: public; Owner: petro
--

SELECT pg_catalog.setval('public.permits_id_seq', 3, true);


--
-- Name: profiles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: petro
--

SELECT pg_catalog.setval('public.profiles_id_seq', 9, true);


--
-- Name: roles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: petro
--

SELECT pg_catalog.setval('public.roles_id_seq', 4, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: petro
--

SELECT pg_catalog.setval('public.users_id_seq', 29, true);


--
-- Name: absens absens_pkey; Type: CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.absens
    ADD CONSTRAINT absens_pkey PRIMARY KEY (id);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: permits permits_pkey; Type: CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.permits
    ADD CONSTRAINT permits_pkey PRIMARY KEY (id);


--
-- Name: profiles profiles_member_id_key; Type: CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.profiles
    ADD CONSTRAINT profiles_member_id_key UNIQUE (member_id);


--
-- Name: profiles profiles_pkey; Type: CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.profiles
    ADD CONSTRAINT profiles_pkey PRIMARY KEY (id);


--
-- Name: roles roles_name_key; Type: CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_name_key UNIQUE (name);


--
-- Name: roles roles_pkey; Type: CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_pkey PRIMARY KEY (id);


--
-- Name: users users_password_key; Type: CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_password_key UNIQUE (password);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: ix_absens_keterangan; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_absens_keterangan ON public.absens USING btree (keterangan);


--
-- Name: ix_permits_keterangan; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_permits_keterangan ON public.permits USING btree (keterangan);


--
-- Name: ix_profiles_address_before; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_profiles_address_before ON public.profiles USING btree (address_before);


--
-- Name: ix_profiles_address_now; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_profiles_address_now ON public.profiles USING btree (address_now);


--
-- Name: ix_profiles_blood; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_profiles_blood ON public.profiles USING btree (blood);


--
-- Name: ix_profiles_gelar; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_profiles_gelar ON public.profiles USING btree (gelar);


--
-- Name: ix_profiles_gender; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_profiles_gender ON public.profiles USING btree (gender);


--
-- Name: ix_profiles_jurusan; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_profiles_jurusan ON public.profiles USING btree (jurusan);


--
-- Name: ix_profiles_married; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_profiles_married ON public.profiles USING btree (married);


--
-- Name: ix_profiles_nik; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_profiles_nik ON public.profiles USING btree (nik);


--
-- Name: ix_profiles_no_hp; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_profiles_no_hp ON public.profiles USING btree (no_hp);


--
-- Name: ix_profiles_npwp; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_profiles_npwp ON public.profiles USING btree (npwp);


--
-- Name: ix_profiles_realname; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_profiles_realname ON public.profiles USING btree (realname);


--
-- Name: ix_profiles_religion; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_profiles_religion ON public.profiles USING btree (religion);


--
-- Name: ix_profiles_study; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_profiles_study ON public.profiles USING btree (study);


--
-- Name: ix_profiles_warga_negara; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_profiles_warga_negara ON public.profiles USING btree (warga_negara);


--
-- Name: ix_profiles_zone; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_profiles_zone ON public.profiles USING btree (zone);


--
-- Name: ix_roles_default; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_roles_default ON public.roles USING btree ("default");


--
-- Name: ix_users_email; Type: INDEX; Schema: public; Owner: petro
--

CREATE UNIQUE INDEX ix_users_email ON public.users USING btree (email);


--
-- Name: ix_users_username; Type: INDEX; Schema: public; Owner: petro
--

CREATE UNIQUE INDEX ix_users_username ON public.users USING btree (username);


--
-- Name: absens absens_member_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.absens
    ADD CONSTRAINT absens_member_id_fkey FOREIGN KEY (member_id) REFERENCES public.users(id);


--
-- Name: permits permits_member_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.permits
    ADD CONSTRAINT permits_member_id_fkey FOREIGN KEY (member_id) REFERENCES public.users(id);


--
-- Name: profiles profiles_member_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.profiles
    ADD CONSTRAINT profiles_member_id_fkey FOREIGN KEY (member_id) REFERENCES public.users(id);


--
-- Name: users users_role_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_role_id_fkey FOREIGN KEY (role_id) REFERENCES public.roles(id);


--
-- PostgreSQL database dump complete
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 12.7
-- Dumped by pg_dump version 12.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: absens; Type: TABLE; Schema: public; Owner: petro
--

CREATE TABLE public.absens (
    id integer NOT NULL,
    dates date,
    jam_datang time without time zone,
    jam_pulang time without time zone,
    keterangan character varying(64),
    member_id integer
);


ALTER TABLE public.absens OWNER TO petro;

--
-- Name: absens_id_seq; Type: SEQUENCE; Schema: public; Owner: petro
--

CREATE SEQUENCE public.absens_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.absens_id_seq OWNER TO petro;

--
-- Name: absens_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: petro
--

ALTER SEQUENCE public.absens_id_seq OWNED BY public.absens.id;


--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: petro
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO petro;

--
-- Name: childs; Type: TABLE; Schema: public; Owner: petro
--

CREATE TABLE public.childs (
    id integer NOT NULL,
    profile_id integer,
    childname character varying(64)
);


ALTER TABLE public.childs OWNER TO petro;

--
-- Name: childs_id_seq; Type: SEQUENCE; Schema: public; Owner: petro
--

CREATE SEQUENCE public.childs_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.childs_id_seq OWNER TO petro;

--
-- Name: childs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: petro
--

ALTER SEQUENCE public.childs_id_seq OWNED BY public.childs.id;


--
-- Name: choices; Type: TABLE; Schema: public; Owner: petro
--

CREATE TABLE public.choices (
    id integer NOT NULL,
    name_choice character varying(64),
    title_choice integer
);


ALTER TABLE public.choices OWNER TO petro;

--
-- Name: choices_id_seq; Type: SEQUENCE; Schema: public; Owner: petro
--

CREATE SEQUENCE public.choices_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.choices_id_seq OWNER TO petro;

--
-- Name: choices_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: petro
--

ALTER SEQUENCE public.choices_id_seq OWNED BY public.choices.id;


--
-- Name: parents; Type: TABLE; Schema: public; Owner: petro
--

CREATE TABLE public.parents (
    id integer NOT NULL,
    profile_id integer,
    parent_name character varying(64),
    status character varying(64),
    parent_address character varying(64)
);


ALTER TABLE public.parents OWNER TO petro;

--
-- Name: parents_id_seq; Type: SEQUENCE; Schema: public; Owner: petro
--

CREATE SEQUENCE public.parents_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.parents_id_seq OWNER TO petro;

--
-- Name: parents_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: petro
--

ALTER SEQUENCE public.parents_id_seq OWNED BY public.parents.id;


--
-- Name: permits; Type: TABLE; Schema: public; Owner: petro
--

CREATE TABLE public.permits (
    id integer NOT NULL,
    long_date integer,
    start_date date,
    keterangan character varying(64),
    disetujui boolean,
    member_id integer
);


ALTER TABLE public.permits OWNER TO petro;

--
-- Name: permits_id_seq; Type: SEQUENCE; Schema: public; Owner: petro
--

CREATE SEQUENCE public.permits_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.permits_id_seq OWNER TO petro;

--
-- Name: permits_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: petro
--

ALTER SEQUENCE public.permits_id_seq OWNED BY public.permits.id;


--
-- Name: profiles; Type: TABLE; Schema: public; Owner: petro
--

CREATE TABLE public.profiles (
    id integer NOT NULL,
    realname character varying(64),
    location character varying(64),
    about_me text,
    study character varying(64),
    jurusan character varying(64),
    gelar character varying(64),
    address_before character varying(64),
    address_now character varying(64),
    blood character varying(64),
    religion character varying(64),
    warga_negara character varying(64),
    nik integer,
    npwp integer,
    no_hp integer,
    zone character varying(64),
    member_id integer,
    gender character varying(64),
    married character varying(64),
    birthday date,
    status_pegawai character varying(64)
);


ALTER TABLE public.profiles OWNER TO petro;

--
-- Name: profiles_id_seq; Type: SEQUENCE; Schema: public; Owner: petro
--

CREATE SEQUENCE public.profiles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.profiles_id_seq OWNER TO petro;

--
-- Name: profiles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: petro
--

ALTER SEQUENCE public.profiles_id_seq OWNED BY public.profiles.id;


--
-- Name: roles; Type: TABLE; Schema: public; Owner: petro
--

CREATE TABLE public.roles (
    id integer NOT NULL,
    name character varying(64),
    "default" boolean,
    permissions integer
);


ALTER TABLE public.roles OWNER TO petro;

--
-- Name: roles_id_seq; Type: SEQUENCE; Schema: public; Owner: petro
--

CREATE SEQUENCE public.roles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.roles_id_seq OWNER TO petro;

--
-- Name: roles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: petro
--

ALTER SEQUENCE public.roles_id_seq OWNED BY public.roles.id;


--
-- Name: timehours; Type: TABLE; Schema: public; Owner: petro
--

CREATE TABLE public.timehours (
    id integer NOT NULL,
    time_start time without time zone,
    time_end time without time zone,
    title_time integer
);


ALTER TABLE public.timehours OWNER TO petro;

--
-- Name: timehours_id_seq; Type: SEQUENCE; Schema: public; Owner: petro
--

CREATE SEQUENCE public.timehours_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.timehours_id_seq OWNER TO petro;

--
-- Name: timehours_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: petro
--

ALTER SEQUENCE public.timehours_id_seq OWNED BY public.timehours.id;


--
-- Name: titles; Type: TABLE; Schema: public; Owner: petro
--

CREATE TABLE public.titles (
    id integer NOT NULL,
    name_title character varying(64)
);


ALTER TABLE public.titles OWNER TO petro;

--
-- Name: titles_id_seq; Type: SEQUENCE; Schema: public; Owner: petro
--

CREATE SEQUENCE public.titles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.titles_id_seq OWNER TO petro;

--
-- Name: titles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: petro
--

ALTER SEQUENCE public.titles_id_seq OWNED BY public.titles.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: petro
--

CREATE TABLE public.users (
    id integer NOT NULL,
    email character varying(64),
    username character varying(64),
    role_id integer,
    confirmed boolean,
    member_since date,
    last_seen timestamp without time zone,
    password character varying(128)
);


ALTER TABLE public.users OWNER TO petro;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: petro
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO petro;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: petro
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: absens id; Type: DEFAULT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.absens ALTER COLUMN id SET DEFAULT nextval('public.absens_id_seq'::regclass);


--
-- Name: childs id; Type: DEFAULT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.childs ALTER COLUMN id SET DEFAULT nextval('public.childs_id_seq'::regclass);


--
-- Name: choices id; Type: DEFAULT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.choices ALTER COLUMN id SET DEFAULT nextval('public.choices_id_seq'::regclass);


--
-- Name: parents id; Type: DEFAULT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.parents ALTER COLUMN id SET DEFAULT nextval('public.parents_id_seq'::regclass);


--
-- Name: permits id; Type: DEFAULT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.permits ALTER COLUMN id SET DEFAULT nextval('public.permits_id_seq'::regclass);


--
-- Name: profiles id; Type: DEFAULT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.profiles ALTER COLUMN id SET DEFAULT nextval('public.profiles_id_seq'::regclass);


--
-- Name: roles id; Type: DEFAULT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.roles ALTER COLUMN id SET DEFAULT nextval('public.roles_id_seq'::regclass);


--
-- Name: timehours id; Type: DEFAULT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.timehours ALTER COLUMN id SET DEFAULT nextval('public.timehours_id_seq'::regclass);


--
-- Name: titles id; Type: DEFAULT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.titles ALTER COLUMN id SET DEFAULT nextval('public.titles_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: absens; Type: TABLE DATA; Schema: public; Owner: petro
--

COPY public.absens (id, dates, jam_datang, jam_pulang, keterangan, member_id) FROM stdin;
2	2021-08-25	07:53:00	16:00:00	semua run absen menu	1
1	2021-08-26	08:28:00	15:15:00	pengerjaan halamn admin	1
3	2021-08-26	15:17:00	\N	\N	5
5	2021-08-23	19:43:00	\N	\N	1
6	2021-08-28	19:46:00	\N	\N	1
4	2021-08-27	19:43:00	19:46:00	test input pulang	1
16	2021-08-28	\N	\N	sakit demam	1
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: petro
--

COPY public.alembic_version (version_num) FROM stdin;
514b3ce26c88
\.


--
-- Data for Name: childs; Type: TABLE DATA; Schema: public; Owner: petro
--

COPY public.childs (id, profile_id, childname) FROM stdin;
\.


--
-- Data for Name: choices; Type: TABLE DATA; Schema: public; Owner: petro
--

COPY public.choices (id, name_choice, title_choice) FROM stdin;
1	R & D Business Development Project	1
2	Air Transport	1
3	Land Transport	1
4	Industry Fuel	1
5	HRGA	1
7	Air Transport Manager	2
8	Direktur	2
9	Cashier	2
10	Chef Assistant	2
11	CRO	2
12	Cook	2
13	Cook Helper	2
14	Manager HRGA & Senior Manager I	2
15	HRGA Staff	2
16	Industrial Fuel Manager & Senior Manager II	2
17	IT Staff	2
18	New Project Manager	2
19	Driver	2
20	Finance Manager	2
21	Ground Crew	2
22	Head Chef	2
23	Land Transportation Manager	2
24	Logistic & Cargo Supervisor	2
25	Marketing	2
26	Non BBM Supervisor	2
27	Office Boy	2
28	Operator	2
29	Public Relation	2
30	Purchasing	2
31	Rider	2
32	Security	2
33	Social Media Content Creator	2
34	Staff Mobil Tangki BBM	2
35	Staff Administrasi	2
36	Supervisor Ground Crew	2
37	Supervisor Mobil Tangki BBM	2
38	Tax Manager & Accounting Staff	2
39	Teknisi	2
40	Bandung	3
41	Laki-laki	6
42	Perempuan	6
43	Pegawai Lepas	4
44	Pegawai Tetap	4
45	Tenaga Kerja Waktu Tertentu/Kontrak	4
46	SD	5
47	SMP	5
48	SMA/SMK (Sederajat)	5
49	Diploma	5
50	Strata I	5
51	Strata II	5
52	Strata III	5
53	A	7
54	B	7
55	AB	7
56	O	7
57	Tidak Tahu	7
58	Islam	8
59	Kristen	8
60	Budha	8
61	Hindu	8
62	Konghuchu	8
63	Lainnya	8
64	Mandiri	11
65	Lainnya	11
66	Ayah	12
67	Ibu	12
68	Suami	12
69	Istri	12
70	Saudara Kandung	12
71	Anak	12
72	Lainnya	12
73	Belum Menikah atau Cerai	10
74	Belum Menikah atau Cerai Memiliki Anak 1	10
75	Belum Menikah atau Cerai Memiliki Anak 2	10
76	Belum Menikah atau Cerai Memiliki Anak 3	10
77	Menikah Belum Memiliki Anak	10
78	Menikah Memiliki Anak 1	10
79	Menikah Memiliki Anak 2	10
80	Menikah Memiliki Anak 3	10
\.


--
-- Data for Name: parents; Type: TABLE DATA; Schema: public; Owner: petro
--

COPY public.parents (id, profile_id, parent_name, status, parent_address) FROM stdin;
\.


--
-- Data for Name: permits; Type: TABLE DATA; Schema: public; Owner: petro
--

COPY public.permits (id, long_date, start_date, keterangan, disetujui, member_id) FROM stdin;
3	12	2021-08-24	izin ke jawa	f	1
2	3	2021-08-25	Jenguk ibu	t	1
4	1	2021-08-28	izin ujang	f	5
\.


--
-- Data for Name: profiles; Type: TABLE DATA; Schema: public; Owner: petro
--

COPY public.profiles (id, realname, location, about_me, study, jurusan, gelar, address_before, address_now, blood, religion, warga_negara, nik, npwp, no_hp, zone, member_id, gender, married, birthday, status_pegawai) FROM stdin;
5	john aja								A		WNI	\N	\N	\N	WIB	1	Pria	Menikah	\N	\N
9	MARDIN WIJAYA	\N		\N	\N	\N	\N	\N	A	\N	WNI	\N	\N	\N	WIB	\N	Pria	Menikah	\N	\N
\.


--
-- Data for Name: roles; Type: TABLE DATA; Schema: public; Owner: petro
--

COPY public.roles (id, name, "default", permissions) FROM stdin;
3	User	t	7
2	Moderator	f	15
1	Admin	f	31
4	Owner	f	63
\.


--
-- Data for Name: timehours; Type: TABLE DATA; Schema: public; Owner: petro
--

COPY public.timehours (id, time_start, time_end, title_time) FROM stdin;
\.


--
-- Data for Name: titles; Type: TABLE DATA; Schema: public; Owner: petro
--

COPY public.titles (id, name_title) FROM stdin;
2	jabatan
3	kantor
1	divisi
4	status kepegawaian
5	pendidikan terakhir
6	jenis kelamin
7	golongan darah
8	agama
9	kewarganegaraan
10	status pernikahan
11	nama bank
12	hubungan wali
13	jam kerja
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: petro
--

COPY public.users (id, email, username, role_id, confirmed, member_since, last_seen, password) FROM stdin;
2	david@example.com	david	4	t	\N	\N	$2a$10$t/sbBm0q0KvoFm2YUHMWteDLyBakryQ0h4A8cCyI1azfDAhcuju/e
33	mardinwijaya46@gmail.com	mardin	3	f	2021-08-27	2021-08-27 21:34:31.853291	$2a$10$R506hr.uC0LhAv91.YOi8OqH1D2cFW.z6p8fd0G/9c6DMuOzovgrq
1	john@example.com	john	1	t	2021-08-23	2021-08-28 14:50:27.605984	$2a$10$mqNoYHRSMCwdx4Xxin8vIuwdqjzVzpBWxeqJpQ0t2PNxDV14lRghq
5	ujang@example.com	ujang	2	t	\N	2021-08-28 14:43:18.974494	$2a$10$llEQQCIjZqy7P1rZPSGuZeVpYsPtIgR0kVYmYHkAp2TV2d/4xIXPC
27	susan@example.com	susan	3	t	2021-08-19	2021-08-26 11:25:21.515718	$2a$10$E3xLAjzGDb2lmn6EyLtJg.OOai7etzux.dinFnDqkzApwN/pJsLRS
\.


--
-- Name: absens_id_seq; Type: SEQUENCE SET; Schema: public; Owner: petro
--

SELECT pg_catalog.setval('public.absens_id_seq', 16, true);


--
-- Name: childs_id_seq; Type: SEQUENCE SET; Schema: public; Owner: petro
--

SELECT pg_catalog.setval('public.childs_id_seq', 1, false);


--
-- Name: choices_id_seq; Type: SEQUENCE SET; Schema: public; Owner: petro
--

SELECT pg_catalog.setval('public.choices_id_seq', 80, true);


--
-- Name: parents_id_seq; Type: SEQUENCE SET; Schema: public; Owner: petro
--

SELECT pg_catalog.setval('public.parents_id_seq', 1, false);


--
-- Name: permits_id_seq; Type: SEQUENCE SET; Schema: public; Owner: petro
--

SELECT pg_catalog.setval('public.permits_id_seq', 4, true);


--
-- Name: profiles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: petro
--

SELECT pg_catalog.setval('public.profiles_id_seq', 9, true);


--
-- Name: roles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: petro
--

SELECT pg_catalog.setval('public.roles_id_seq', 4, true);


--
-- Name: timehours_id_seq; Type: SEQUENCE SET; Schema: public; Owner: petro
--

SELECT pg_catalog.setval('public.timehours_id_seq', 1, false);


--
-- Name: titles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: petro
--

SELECT pg_catalog.setval('public.titles_id_seq', 13, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: petro
--

SELECT pg_catalog.setval('public.users_id_seq', 33, true);


--
-- Name: absens absens_pkey; Type: CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.absens
    ADD CONSTRAINT absens_pkey PRIMARY KEY (id);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: childs childs_pkey; Type: CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.childs
    ADD CONSTRAINT childs_pkey PRIMARY KEY (id);


--
-- Name: choices choices_pkey; Type: CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.choices
    ADD CONSTRAINT choices_pkey PRIMARY KEY (id);


--
-- Name: parents parents_pkey; Type: CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.parents
    ADD CONSTRAINT parents_pkey PRIMARY KEY (id);


--
-- Name: permits permits_pkey; Type: CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.permits
    ADD CONSTRAINT permits_pkey PRIMARY KEY (id);


--
-- Name: profiles profiles_member_id_key; Type: CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.profiles
    ADD CONSTRAINT profiles_member_id_key UNIQUE (member_id);


--
-- Name: profiles profiles_pkey; Type: CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.profiles
    ADD CONSTRAINT profiles_pkey PRIMARY KEY (id);


--
-- Name: roles roles_name_key; Type: CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_name_key UNIQUE (name);


--
-- Name: roles roles_pkey; Type: CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_pkey PRIMARY KEY (id);


--
-- Name: timehours timehours_pkey; Type: CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.timehours
    ADD CONSTRAINT timehours_pkey PRIMARY KEY (id);


--
-- Name: titles titles_pkey; Type: CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.titles
    ADD CONSTRAINT titles_pkey PRIMARY KEY (id);


--
-- Name: users users_password_key; Type: CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_password_key UNIQUE (password);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: ix_absens_keterangan; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_absens_keterangan ON public.absens USING btree (keterangan);


--
-- Name: ix_childs_childname; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_childs_childname ON public.childs USING btree (childname);


--
-- Name: ix_choices_name_choice; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_choices_name_choice ON public.choices USING btree (name_choice);


--
-- Name: ix_parents_parent_address; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_parents_parent_address ON public.parents USING btree (parent_address);


--
-- Name: ix_parents_parent_name; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_parents_parent_name ON public.parents USING btree (parent_name);


--
-- Name: ix_parents_status; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_parents_status ON public.parents USING btree (status);


--
-- Name: ix_permits_keterangan; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_permits_keterangan ON public.permits USING btree (keterangan);


--
-- Name: ix_profiles_address_before; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_profiles_address_before ON public.profiles USING btree (address_before);


--
-- Name: ix_profiles_address_now; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_profiles_address_now ON public.profiles USING btree (address_now);


--
-- Name: ix_profiles_blood; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_profiles_blood ON public.profiles USING btree (blood);


--
-- Name: ix_profiles_gelar; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_profiles_gelar ON public.profiles USING btree (gelar);


--
-- Name: ix_profiles_gender; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_profiles_gender ON public.profiles USING btree (gender);


--
-- Name: ix_profiles_jurusan; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_profiles_jurusan ON public.profiles USING btree (jurusan);


--
-- Name: ix_profiles_married; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_profiles_married ON public.profiles USING btree (married);


--
-- Name: ix_profiles_nik; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_profiles_nik ON public.profiles USING btree (nik);


--
-- Name: ix_profiles_no_hp; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_profiles_no_hp ON public.profiles USING btree (no_hp);


--
-- Name: ix_profiles_npwp; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_profiles_npwp ON public.profiles USING btree (npwp);


--
-- Name: ix_profiles_realname; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_profiles_realname ON public.profiles USING btree (realname);


--
-- Name: ix_profiles_religion; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_profiles_religion ON public.profiles USING btree (religion);


--
-- Name: ix_profiles_status_pegawai; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_profiles_status_pegawai ON public.profiles USING btree (status_pegawai);


--
-- Name: ix_profiles_study; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_profiles_study ON public.profiles USING btree (study);


--
-- Name: ix_profiles_warga_negara; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_profiles_warga_negara ON public.profiles USING btree (warga_negara);


--
-- Name: ix_profiles_zone; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_profiles_zone ON public.profiles USING btree (zone);


--
-- Name: ix_roles_default; Type: INDEX; Schema: public; Owner: petro
--

CREATE INDEX ix_roles_default ON public.roles USING btree ("default");


--
-- Name: ix_titles_name_title; Type: INDEX; Schema: public; Owner: petro
--

CREATE UNIQUE INDEX ix_titles_name_title ON public.titles USING btree (name_title);


--
-- Name: ix_users_email; Type: INDEX; Schema: public; Owner: petro
--

CREATE UNIQUE INDEX ix_users_email ON public.users USING btree (email);


--
-- Name: ix_users_username; Type: INDEX; Schema: public; Owner: petro
--

CREATE UNIQUE INDEX ix_users_username ON public.users USING btree (username);


--
-- Name: absens absens_member_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.absens
    ADD CONSTRAINT absens_member_id_fkey FOREIGN KEY (member_id) REFERENCES public.users(id);


--
-- Name: childs childs_profile_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.childs
    ADD CONSTRAINT childs_profile_id_fkey FOREIGN KEY (profile_id) REFERENCES public.profiles(id);


--
-- Name: choices choices_title_choice_fkey; Type: FK CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.choices
    ADD CONSTRAINT choices_title_choice_fkey FOREIGN KEY (title_choice) REFERENCES public.titles(id);


--
-- Name: parents parents_profile_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.parents
    ADD CONSTRAINT parents_profile_id_fkey FOREIGN KEY (profile_id) REFERENCES public.profiles(id);


--
-- Name: permits permits_member_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.permits
    ADD CONSTRAINT permits_member_id_fkey FOREIGN KEY (member_id) REFERENCES public.users(id);


--
-- Name: profiles profiles_member_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.profiles
    ADD CONSTRAINT profiles_member_id_fkey FOREIGN KEY (member_id) REFERENCES public.users(id);


--
-- Name: timehours timehours_title_time_fkey; Type: FK CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.timehours
    ADD CONSTRAINT timehours_title_time_fkey FOREIGN KEY (title_time) REFERENCES public.titles(id);


--
-- Name: users users_role_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_role_id_fkey FOREIGN KEY (role_id) REFERENCES public.roles(id);


--
-- PostgreSQL database dump complete
--

