--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: coach; Type: TABLE; Schema: public; Owner: vagrant; Tablespace: 
--

CREATE TABLE coach (
    objectid integer NOT NULL,
    name character varying,
    surname character varying,
    countryid integer,
    teamid integer,
    birthday date,
    genderid integer,
    deleted integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.coach OWNER TO vagrant;

--
-- Name: coach_objectid_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE coach_objectid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.coach_objectid_seq OWNER TO vagrant;

--
-- Name: coach_objectid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE coach_objectid_seq OWNED BY coach.objectid;


--
-- Name: country; Type: TABLE; Schema: public; Owner: vagrant; Tablespace: 
--

CREATE TABLE country (
    objectid integer NOT NULL,
    name character varying,
    deleted integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.country OWNER TO vagrant;

--
-- Name: country_objectid_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE country_objectid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.country_objectid_seq OWNER TO vagrant;

--
-- Name: country_objectid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE country_objectid_seq OWNED BY country.objectid;


--
-- Name: court; Type: TABLE; Schema: public; Owner: vagrant; Tablespace: 
--

CREATE TABLE court (
    objectid integer NOT NULL,
    name character varying,
    address character varying,
    capacity numeric,
    deleted integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.court OWNER TO vagrant;

--
-- Name: court_objectid_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE court_objectid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.court_objectid_seq OWNER TO vagrant;

--
-- Name: court_objectid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE court_objectid_seq OWNED BY court.objectid;


--
-- Name: gender; Type: TABLE; Schema: public; Owner: vagrant; Tablespace: 
--

CREATE TABLE gender (
    objectid integer NOT NULL,
    type character varying,
    deleted integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.gender OWNER TO vagrant;

--
-- Name: gender_objectid_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE gender_objectid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.gender_objectid_seq OWNER TO vagrant;

--
-- Name: gender_objectid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE gender_objectid_seq OWNED BY gender.objectid;


--
-- Name: hand; Type: TABLE; Schema: public; Owner: vagrant; Tablespace: 
--

CREATE TABLE hand (
    objectid integer NOT NULL,
    name character varying,
    deleted integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.hand OWNER TO vagrant;

--
-- Name: hand_objectid_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE hand_objectid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.hand_objectid_seq OWNER TO vagrant;

--
-- Name: hand_objectid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE hand_objectid_seq OWNED BY hand.objectid;


--
-- Name: match; Type: TABLE; Schema: public; Owner: vagrant; Tablespace: 
--

CREATE TABLE match (
    objectid integer NOT NULL,
    hometeamid integer,
    awayteamid integer,
    courtid integer,
    matchdate date,
    deleted integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.match OWNER TO vagrant;

--
-- Name: match_objectid_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE match_objectid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.match_objectid_seq OWNER TO vagrant;

--
-- Name: match_objectid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE match_objectid_seq OWNED BY match.objectid;


--
-- Name: player; Type: TABLE; Schema: public; Owner: vagrant; Tablespace: 
--

CREATE TABLE player (
    objectid integer NOT NULL,
    name character varying,
    surname character varying,
    birthdate date,
    height numeric,
    weight numeric,
    startdate date,
    teamid integer,
    countryid integer,
    genderid integer,
    positionid integer,
    handid integer,
    number integer,
    deleted integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.player OWNER TO vagrant;

--
-- Name: player_objectid_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE player_objectid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.player_objectid_seq OWNER TO vagrant;

--
-- Name: player_objectid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE player_objectid_seq OWNED BY player.objectid;


--
-- Name: position; Type: TABLE; Schema: public; Owner: vagrant; Tablespace: 
--

CREATE TABLE "position" (
    objectid integer NOT NULL,
    name character varying,
    deleted integer DEFAULT 0 NOT NULL
);


ALTER TABLE public."position" OWNER TO vagrant;

--
-- Name: position_objectid_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE position_objectid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.position_objectid_seq OWNER TO vagrant;

--
-- Name: position_objectid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE position_objectid_seq OWNED BY "position".objectid;


--
-- Name: season; Type: TABLE; Schema: public; Owner: vagrant; Tablespace: 
--

CREATE TABLE season (
    objectid integer NOT NULL,
    name character varying,
    deleted integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.season OWNER TO vagrant;

--
-- Name: season_objectid_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE season_objectid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.season_objectid_seq OWNER TO vagrant;

--
-- Name: season_objectid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE season_objectid_seq OWNED BY season.objectid;


--
-- Name: statistic; Type: TABLE; Schema: public; Owner: vagrant; Tablespace: 
--

CREATE TABLE statistic (
    objectid integer NOT NULL,
    assistnumber integer,
    blocknumber integer,
    score integer,
    cardnumber integer,
    seasonid integer,
    playerid integer,
    deleted integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.statistic OWNER TO vagrant;

--
-- Name: statistic_objectid_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE statistic_objectid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.statistic_objectid_seq OWNER TO vagrant;

--
-- Name: statistic_objectid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE statistic_objectid_seq OWNED BY statistic.objectid;


--
-- Name: team; Type: TABLE; Schema: public; Owner: vagrant; Tablespace: 
--

CREATE TABLE team (
    objectid integer NOT NULL,
    name character varying,
    shirtcolour character varying,
    foundationdate date,
    countryid integer,
    courtid integer,
    deleted integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.team OWNER TO vagrant;

--
-- Name: team_objectid_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE team_objectid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.team_objectid_seq OWNER TO vagrant;

--
-- Name: team_objectid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE team_objectid_seq OWNED BY team.objectid;


--
-- Name: transfer; Type: TABLE; Schema: public; Owner: vagrant; Tablespace: 
--

CREATE TABLE transfer (
    objectid integer NOT NULL,
    playerid integer,
    oldteamid integer,
    newteamid integer,
    seasonid integer,
    deleted integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.transfer OWNER TO vagrant;

--
-- Name: transfer_objectid_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE transfer_objectid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.transfer_objectid_seq OWNER TO vagrant;

--
-- Name: transfer_objectid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE transfer_objectid_seq OWNED BY transfer.objectid;


--
-- Name: userinformation; Type: TABLE; Schema: public; Owner: vagrant; Tablespace: 
--

CREATE TABLE userinformation (
    objectid integer NOT NULL,
    favoriteteamid integer,
    name character varying,
    surname character varying,
    birthdate date,
    deleted integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.userinformation OWNER TO vagrant;

--
-- Name: userinformation_objectid_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE userinformation_objectid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.userinformation_objectid_seq OWNER TO vagrant;

--
-- Name: userinformation_objectid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE userinformation_objectid_seq OWNED BY userinformation.objectid;


--
-- Name: userrole; Type: TABLE; Schema: public; Owner: vagrant; Tablespace: 
--

CREATE TABLE userrole (
    objectid integer NOT NULL,
    name character varying,
    deleted integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.userrole OWNER TO vagrant;

--
-- Name: userrole_objectid_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE userrole_objectid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.userrole_objectid_seq OWNER TO vagrant;

--
-- Name: userrole_objectid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE userrole_objectid_seq OWNED BY userrole.objectid;


--
-- Name: usertable; Type: TABLE; Schema: public; Owner: vagrant; Tablespace: 
--

CREATE TABLE usertable (
    objectid integer NOT NULL,
    username character varying,
    password bytea,
    userroleid integer,
    userinformationid integer,
    deleted integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.usertable OWNER TO vagrant;

--
-- Name: usertable_objectid_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE usertable_objectid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.usertable_objectid_seq OWNER TO vagrant;

--
-- Name: usertable_objectid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE usertable_objectid_seq OWNED BY usertable.objectid;


--
-- Name: objectid; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY coach ALTER COLUMN objectid SET DEFAULT nextval('coach_objectid_seq'::regclass);


--
-- Name: objectid; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY country ALTER COLUMN objectid SET DEFAULT nextval('country_objectid_seq'::regclass);


--
-- Name: objectid; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY court ALTER COLUMN objectid SET DEFAULT nextval('court_objectid_seq'::regclass);


--
-- Name: objectid; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY gender ALTER COLUMN objectid SET DEFAULT nextval('gender_objectid_seq'::regclass);


--
-- Name: objectid; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY hand ALTER COLUMN objectid SET DEFAULT nextval('hand_objectid_seq'::regclass);


--
-- Name: objectid; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY match ALTER COLUMN objectid SET DEFAULT nextval('match_objectid_seq'::regclass);


--
-- Name: objectid; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY player ALTER COLUMN objectid SET DEFAULT nextval('player_objectid_seq'::regclass);


--
-- Name: objectid; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY "position" ALTER COLUMN objectid SET DEFAULT nextval('position_objectid_seq'::regclass);


--
-- Name: objectid; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY season ALTER COLUMN objectid SET DEFAULT nextval('season_objectid_seq'::regclass);


--
-- Name: objectid; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY statistic ALTER COLUMN objectid SET DEFAULT nextval('statistic_objectid_seq'::regclass);


--
-- Name: objectid; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY team ALTER COLUMN objectid SET DEFAULT nextval('team_objectid_seq'::regclass);


--
-- Name: objectid; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY transfer ALTER COLUMN objectid SET DEFAULT nextval('transfer_objectid_seq'::regclass);


--
-- Name: objectid; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY userinformation ALTER COLUMN objectid SET DEFAULT nextval('userinformation_objectid_seq'::regclass);


--
-- Name: objectid; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY userrole ALTER COLUMN objectid SET DEFAULT nextval('userrole_objectid_seq'::regclass);


--
-- Name: objectid; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY usertable ALTER COLUMN objectid SET DEFAULT nextval('usertable_objectid_seq'::regclass);


--
-- Data for Name: coach; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY coach (objectid, name, surname, countryid, teamid, birthday, genderid, deleted) FROM stdin;
1	Ergin	Ataman	1	1	1970-10-30	1	0
\.


--
-- Name: coach_objectid_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('coach_objectid_seq', 1, true);


--
-- Data for Name: country; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY country (objectid, name, deleted) FROM stdin;
1	Turkey	0
\.


--
-- Name: country_objectid_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('country_objectid_seq', 1, true);


--
-- Data for Name: court; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY court (objectid, name, address, capacity, deleted) FROM stdin;
1	Abdi İpekçi	Maslak Arena	20000	0
2	Ülker Arena	Bağcılar	3000	0
\.


--
-- Name: court_objectid_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('court_objectid_seq', 2, true);


--
-- Data for Name: gender; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY gender (objectid, type, deleted) FROM stdin;
1	Male	0
2	Female	0
\.


--
-- Name: gender_objectid_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('gender_objectid_seq', 2, true);


--
-- Data for Name: hand; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY hand (objectid, name, deleted) FROM stdin;
1	Left	0
2	Right	0
\.


--
-- Name: hand_objectid_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('hand_objectid_seq', 2, true);


--
-- Data for Name: match; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY match (objectid, hometeamid, awayteamid, courtid, matchdate, deleted) FROM stdin;
1	1	2	1	2015-10-30	0
\.


--
-- Name: match_objectid_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('match_objectid_seq', 1, true);


--
-- Data for Name: player; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY player (objectid, name, surname, birthdate, height, weight, startdate, teamid, countryid, genderid, positionid, handid, number, deleted) FROM stdin;
1	Neslihan	Darnel	1980-10-30	185	70	2000-10-30	1	1	2	1	2	8	0
\.


--
-- Name: player_objectid_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('player_objectid_seq', 1, true);


--
-- Data for Name: position; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY "position" (objectid, name, deleted) FROM stdin;
1	Center	0
\.


--
-- Name: position_objectid_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('position_objectid_seq', 1, true);


--
-- Data for Name: season; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY season (objectid, name, deleted) FROM stdin;
1	2014-2015	0
\.


--
-- Name: season_objectid_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('season_objectid_seq', 1, true);


--
-- Data for Name: statistic; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY statistic (objectid, assistnumber, blocknumber, score, cardnumber, seasonid, playerid, deleted) FROM stdin;
1	30	15	212	2	1	1	0
\.


--
-- Name: statistic_objectid_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('statistic_objectid_seq', 1, true);


--
-- Data for Name: team; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY team (objectid, name, shirtcolour, foundationdate, countryid, courtid, deleted) FROM stdin;
1	Galatasaray	Red-Yellow	1905-05-30	1	1	0
2	Fenerbahçe	Yellow-blue	1907-08-30	1	2	0
\.


--
-- Name: team_objectid_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('team_objectid_seq', 2, true);


--
-- Data for Name: transfer; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY transfer (objectid, playerid, oldteamid, newteamid, seasonid, deleted) FROM stdin;
1	1	1	2	1	0
\.


--
-- Name: transfer_objectid_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('transfer_objectid_seq', 1, true);


--
-- Data for Name: userinformation; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY userinformation (objectid, favoriteteamid, name, surname, birthdate, deleted) FROM stdin;
1	1	İsmail Tunahan	Er	1994-09-18	0
\.


--
-- Name: userinformation_objectid_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('userinformation_objectid_seq', 1, true);


--
-- Data for Name: userrole; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY userrole (objectid, name, deleted) FROM stdin;
1	Administrator	0
\.


--
-- Name: userrole_objectid_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('userrole_objectid_seq', 1, true);


--
-- Data for Name: usertable; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY usertable (objectid, username, password, userroleid, userinformationid, deleted) FROM stdin;
1	erism	\\x3132333435	1	1	0
\.


--
-- Name: usertable_objectid_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('usertable_objectid_seq', 1, true);


--
-- Name: coach_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant; Tablespace: 
--

ALTER TABLE ONLY coach
    ADD CONSTRAINT coach_pkey PRIMARY KEY (objectid);


--
-- Name: country_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant; Tablespace: 
--

ALTER TABLE ONLY country
    ADD CONSTRAINT country_pkey PRIMARY KEY (objectid);


--
-- Name: court_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant; Tablespace: 
--

ALTER TABLE ONLY court
    ADD CONSTRAINT court_pkey PRIMARY KEY (objectid);


--
-- Name: gender_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant; Tablespace: 
--

ALTER TABLE ONLY gender
    ADD CONSTRAINT gender_pkey PRIMARY KEY (objectid);


--
-- Name: hand_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant; Tablespace: 
--

ALTER TABLE ONLY hand
    ADD CONSTRAINT hand_pkey PRIMARY KEY (objectid);


--
-- Name: match_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant; Tablespace: 
--

ALTER TABLE ONLY match
    ADD CONSTRAINT match_pkey PRIMARY KEY (objectid);


--
-- Name: player_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant; Tablespace: 
--

ALTER TABLE ONLY player
    ADD CONSTRAINT player_pkey PRIMARY KEY (objectid);


--
-- Name: position_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant; Tablespace: 
--

ALTER TABLE ONLY "position"
    ADD CONSTRAINT position_pkey PRIMARY KEY (objectid);


--
-- Name: season_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant; Tablespace: 
--

ALTER TABLE ONLY season
    ADD CONSTRAINT season_pkey PRIMARY KEY (objectid);


--
-- Name: statistic_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant; Tablespace: 
--

ALTER TABLE ONLY statistic
    ADD CONSTRAINT statistic_pkey PRIMARY KEY (objectid);


--
-- Name: team_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant; Tablespace: 
--

ALTER TABLE ONLY team
    ADD CONSTRAINT team_pkey PRIMARY KEY (objectid);


--
-- Name: transfer_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant; Tablespace: 
--

ALTER TABLE ONLY transfer
    ADD CONSTRAINT transfer_pkey PRIMARY KEY (objectid);


--
-- Name: userinformation_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant; Tablespace: 
--

ALTER TABLE ONLY userinformation
    ADD CONSTRAINT userinformation_pkey PRIMARY KEY (objectid);


--
-- Name: userrole_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant; Tablespace: 
--

ALTER TABLE ONLY userrole
    ADD CONSTRAINT userrole_pkey PRIMARY KEY (objectid);


--
-- Name: usertable_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant; Tablespace: 
--

ALTER TABLE ONLY usertable
    ADD CONSTRAINT usertable_pkey PRIMARY KEY (objectid);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--
