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
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: petro
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO petro;

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
    password_hash character varying(128),
    confirmed boolean,
    name character varying(64),
    location character varying(64),
    about_me text,
    member_since timestamp without time zone,
    last_seen timestamp without time zone
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
-- Name: roles id; Type: DEFAULT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.roles ALTER COLUMN id SET DEFAULT nextval('public.roles_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: petro
--

COPY public.alembic_version (version_num) FROM stdin;
77cfbfde1ea7
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

COPY public.users (id, email, username, role_id, password_hash, confirmed, name, location, about_me, member_since, last_seen) FROM stdin;
2	david@example.com	david	4	$2a$10$vyuSo0EnXWDinldId/Zh7O5fRF3TPnDY34tXlUv82Lrkf7ilxiCjm	t	David Own	jakarta	ini owner	\N	2021-08-04 13:53:21.092154
4	mardinw26@gmail.com	mardin	3	$2a$10$0RQPA/eJgjmaE02gfkOrbeukYdDIrKpKQ6HxFCvtkAKVOv6hbXmEC	t	Mardin Wijaya	Bandung	Ini tulisan tentang about profile	\N	2021-08-04 13:49:19.544225
3	susan@example.com	susan	3	$2a$10$LVcP6MogYKsDaAC3cfuBtOJ2n/EVEw4e175sWNPt8y0MrzpWR4uoy	\N	\N	\N	\N	\N	\N
5	ujang@example.com	ujang	2	$2a$10$GUfpuqrrFnBC5vVa23y0Quz6nYJhzVcKqW6asuhXRAxar9btUgxiW	t	\N	\N	\N	\N	2021-08-04 14:32:55.234281
1	john@example.com	john	1	$2a$10$LYawcPvdiRWbwrIcqG1St.8UMOXdkLm65SQiaX1yl.hmPf69FeBxK	t	\N	\N	\N	\N	2021-08-04 14:34:24.762577
\.


--
-- Name: roles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: petro
--

SELECT pg_catalog.setval('public.roles_id_seq', 4, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: petro
--

SELECT pg_catalog.setval('public.users_id_seq', 26, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


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
-- Name: users users_password_hash_key; Type: CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_password_hash_key UNIQUE (password_hash);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


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
-- Name: users users_role_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: petro
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_role_id_fkey FOREIGN KEY (role_id) REFERENCES public.roles(id);


--
-- PostgreSQL database dump complete
--

