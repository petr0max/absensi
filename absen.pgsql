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

