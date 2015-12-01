--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

ALTER TABLE IF EXISTS ONLY public.usertable DROP CONSTRAINT IF EXISTS usertable_userroleid_fkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.usertable DROP CONSTRAINT IF EXISTS usertable_userinformationid_fkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.userinformation DROP CONSTRAINT IF EXISTS userinformation_favoriteteamid_fkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.transfer DROP CONSTRAINT IF EXISTS transfer_seasonid_fkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.transfer DROP CONSTRAINT IF EXISTS transfer_playerid_fkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.transfer DROP CONSTRAINT IF EXISTS transfer_oldteamid_fkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.transfer DROP CONSTRAINT IF EXISTS transfer_newteamid_fkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.team DROP CONSTRAINT IF EXISTS team_courtid_fkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.team DROP CONSTRAINT IF EXISTS team_countryid_fkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.statistic DROP CONSTRAINT IF EXISTS statistic_seasonid_fkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.statistic DROP CONSTRAINT IF EXISTS statistic_playerid_fkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.player DROP CONSTRAINT IF EXISTS player_teamid_fkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.player DROP CONSTRAINT IF EXISTS player_positionid_fkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.player DROP CONSTRAINT IF EXISTS player_handid_fkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.player DROP CONSTRAINT IF EXISTS player_genderid_fkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.player DROP CONSTRAINT IF EXISTS player_countryid_fkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.match DROP CONSTRAINT IF EXISTS match_hometeamid_fkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.match DROP CONSTRAINT IF EXISTS match_courtid_fkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.match DROP CONSTRAINT IF EXISTS match_awayteamid_fkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.coach DROP CONSTRAINT IF EXISTS coach_teamid_fkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.coach DROP CONSTRAINT IF EXISTS coach_genderid_fkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.coach DROP CONSTRAINT IF EXISTS coach_countryid_fkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.usertable DROP CONSTRAINT IF EXISTS usertable_pkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.userrole DROP CONSTRAINT IF EXISTS userrole_pkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.userinformation DROP CONSTRAINT IF EXISTS userinformation_pkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.transfer DROP CONSTRAINT IF EXISTS transfer_pkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.team DROP CONSTRAINT IF EXISTS team_pkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.statistic DROP CONSTRAINT IF EXISTS statistic_pkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.season DROP CONSTRAINT IF EXISTS season_pkey CASCADE;
ALTER TABLE IF EXISTS ONLY public."position" DROP CONSTRAINT IF EXISTS position_pkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.player DROP CONSTRAINT IF EXISTS player_pkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.match DROP CONSTRAINT IF EXISTS match_pkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.hand DROP CONSTRAINT IF EXISTS hand_pkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.gender DROP CONSTRAINT IF EXISTS gender_pkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.court DROP CONSTRAINT IF EXISTS court_pkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.country DROP CONSTRAINT IF EXISTS country_pkey CASCADE;
ALTER TABLE IF EXISTS ONLY public.coach DROP CONSTRAINT coach_pkey CASCADE;
ALTER TABLE IF EXISTS public.usertable ALTER COLUMN objectid DROP DEFAULT;
ALTER TABLE IF EXISTS public.userrole ALTER COLUMN objectid DROP DEFAULT;
ALTER TABLE IF EXISTS public.userinformation ALTER COLUMN objectid DROP DEFAULT;
ALTER TABLE IF EXISTS public.transfer ALTER COLUMN objectid DROP DEFAULT;
ALTER TABLE IF EXISTS public.team ALTER COLUMN objectid DROP DEFAULT;
ALTER TABLE IF EXISTS public.statistic ALTER COLUMN objectid DROP DEFAULT;
ALTER TABLE IF EXISTS public.season ALTER COLUMN objectid DROP DEFAULT;
ALTER TABLE IF EXISTS public."position" ALTER COLUMN objectid DROP DEFAULT;
ALTER TABLE IF EXISTS public.player ALTER COLUMN objectid DROP DEFAULT;
ALTER TABLE IF EXISTS public.match ALTER COLUMN objectid DROP DEFAULT;
ALTER TABLE IF EXISTS public.hand ALTER COLUMN objectid DROP DEFAULT;
ALTER TABLE IF EXISTS public.gender ALTER COLUMN objectid DROP DEFAULT;
ALTER TABLE IF EXISTS public.court ALTER COLUMN objectid DROP DEFAULT;
ALTER TABLE IF EXISTS public.country ALTER COLUMN objectid DROP DEFAULT;
ALTER TABLE IF EXISTS public.coach ALTER COLUMN objectid DROP DEFAULT;
DROP SEQUENCE IF EXISTS public.usertable_objectid_seq CASCADE;
DROP TABLE IF EXISTS public.usertable CASCADE;
DROP SEQUENCE IF EXISTS public.userrole_objectid_seq CASCADE;
DROP TABLE IF EXISTS public.userrole CASCADE;
DROP SEQUENCE IF EXISTS public.userinformation_objectid_seq CASCADE;
DROP TABLE IF EXISTS public.userinformation CASCADE;
DROP SEQUENCE IF EXISTS public.transfer_objectid_seq CASCADE;
DROP TABLE IF EXISTS public.transfer CASCADE;
DROP SEQUENCE IF EXISTS public.team_objectid_seq CASCADE;
DROP TABLE IF EXISTS public.team CASCADE;
DROP SEQUENCE IF EXISTS public.statistic_objectid_seq CASCADE;
DROP TABLE IF EXISTS public.statistic CASCADE;
DROP SEQUENCE IF EXISTS public.season_objectid_seq CASCADE;
DROP TABLE IF EXISTS public.season CASCADE;
DROP SEQUENCE IF EXISTS public.position_objectid_seq CASCADE;
DROP TABLE IF EXISTS public."position" CASCADE; 
DROP SEQUENCE IF EXISTS public.player_objectid_seq CASCADE;
DROP TABLE IF EXISTS public.player CASCADE;
DROP SEQUENCE IF EXISTS public.match_objectid_seq CASCADE;
DROP TABLE IF EXISTS public.match CASCADE;
DROP SEQUENCE IF EXISTS public.hand_objectid_seq CASCADE;
DROP TABLE IF EXISTS public.hand CASCADE;
DROP SEQUENCE IF EXISTS public.gender_objectid_seq CASCADE;
DROP TABLE IF EXISTS public.gender CASCADE;
DROP SEQUENCE IF EXISTS public.court_objectid_seq CASCADE;
DROP TABLE IF EXISTS public.court CASCADE;
DROP SEQUENCE IF EXISTS public.country_objectid_seq CASCADE;
DROP TABLE IF EXISTS public.country CASCADE;
DROP SEQUENCE IF EXISTS public.coach_objectid_seq CASCADE;
DROP TABLE IF EXISTS public.coach CASCADE;



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


--ALTER TABLE public.coach OWNER TO vagrant;

--
-- Name: coach_objectid_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE coach_objectid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--ALTER TABLE public.coach_objectid_seq OWNER TO vagrant;

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


--ALTER TABLE public.country OWNER TO vagrant;

--
-- Name: country_objectid_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE country_objectid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--ALTER TABLE public.country_objectid_seq OWNER TO vagrant;

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


--ALTER TABLE public.court OWNER TO vagrant;

--
-- Name: court_objectid_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE court_objectid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--ALTER TABLE public.court_objectid_seq OWNER TO vagrant;

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


--ALTER TABLE public.gender OWNER TO vagrant;

--
-- Name: gender_objectid_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE gender_objectid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--ALTER TABLE public.gender_objectid_seq OWNER TO vagrant;

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


--ALTER TABLE public.hand OWNER TO vagrant;

--
-- Name: hand_objectid_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE hand_objectid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--ALTER TABLE public.hand_objectid_seq OWNER TO vagrant;

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


--ALTER TABLE public.match OWNER TO vagrant;

--
-- Name: match_objectid_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE match_objectid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--ALTER TABLE public.match_objectid_seq OWNER TO vagrant;

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


--ALTER TABLE public.player OWNER TO vagrant;

--
-- Name: player_objectid_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE player_objectid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--ALTER TABLE public.player_objectid_seq OWNER TO vagrant;

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


--ALTER TABLE public."position" OWNER TO vagrant;

--
-- Name: position_objectid_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE position_objectid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--ALTER TABLE public.position_objectid_seq OWNER TO vagrant;

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


--ALTER TABLE public.season OWNER TO vagrant;

--
-- Name: season_objectid_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE season_objectid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--ALTER TABLE public.season_objectid_seq OWNER TO vagrant;

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


--ALTER TABLE public.statistic OWNER TO vagrant;

--
-- Name: statistic_objectid_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE statistic_objectid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--ALTER TABLE public.statistic_objectid_seq OWNER TO vagrant;

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


--ALTER TABLE public.team OWNER TO vagrant;

--
-- Name: team_objectid_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE team_objectid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--ALTER TABLE public.team_objectid_seq OWNER TO vagrant;

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


--ALTER TABLE public.transfer OWNER TO vagrant;

--
-- Name: transfer_objectid_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE transfer_objectid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--ALTER TABLE public.transfer_objectid_seq OWNER TO vagrant;

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


--ALTER TABLE public.userinformation OWNER TO vagrant;

--
-- Name: userinformation_objectid_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE userinformation_objectid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--ALTER TABLE public.userinformation_objectid_seq OWNER TO vagrant;

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


--ALTER TABLE public.userrole OWNER TO vagrant;

--
-- Name: userrole_objectid_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE userrole_objectid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--ALTER TABLE public.userrole_objectid_seq OWNER TO vagrant;

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


--ALTER TABLE public.usertable OWNER TO vagrant;

--
-- Name: usertable_objectid_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE usertable_objectid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--ALTER TABLE public.usertable_objectid_seq OWNER TO vagrant;

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

INSERT INTO coach VALUES (1, 'Ataman', 'Güneyligil', 3, 1, '1970-12-10', 1, 0);
INSERT INTO coach VALUES (2, 'Marcello ', 'Abbondanza', 8, 2, '1970-12-10', 1, 0);
INSERT INTO coach VALUES (3, 'Giovanni ', 'Guidetti', 8, 3, '1970-12-10', 1, 0);


--
-- Name: coach_objectid_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('coach_objectid_seq', 3, true);


--
-- Data for Name: country; Type: TABLE DATA; Schema: public; Owner: vagrant
--

INSERT INTO country VALUES (3, 'Turkey', 0);
INSERT INTO country VALUES (4, 'England', 0);
INSERT INTO country VALUES (5, 'Spain', 0);
INSERT INTO country VALUES (8, 'Italy', 0);


--
-- Name: country_objectid_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('country_objectid_seq', 8, true);


--
-- Data for Name: court; Type: TABLE DATA; Schema: public; Owner: vagrant
--

INSERT INTO court VALUES (1, 'Burhan Felek Spor Salonu', 'Üsküdar, İstanbul', 7500, 0);
INSERT INTO court VALUES (2, 'Muhtar Sencer Sports Center', 'Kadıköy, İstanbul', 7500, 0);
INSERT INTO court VALUES (3, 'Santiago Bernabéu', 'Madrid, Spain', 12000, 0);
INSERT INTO court VALUES (4, 'Vakıfbank Spor Sarayı', 'Üsküdar, İstanbul', 2500, 0);
INSERT INTO court VALUES (5, 'Eczacıbaşı Sport Center', 'Ayazağa, İstanbul', 1000, 0);


--
-- Name: court_objectid_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('court_objectid_seq', 5, true);


--
-- Data for Name: gender; Type: TABLE DATA; Schema: public; Owner: vagrant
--

INSERT INTO gender VALUES (1, 'Male', 0);
INSERT INTO gender VALUES (2, 'Female', 0);


--
-- Name: gender_objectid_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('gender_objectid_seq', 2, true);


--
-- Data for Name: hand; Type: TABLE DATA; Schema: public; Owner: vagrant
--

INSERT INTO hand VALUES (1, 'Left', 0);
INSERT INTO hand VALUES (2, 'Right', 0);
INSERT INTO hand VALUES (4, 'Both', 0);


--
-- Name: hand_objectid_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('hand_objectid_seq', 4, true);


--
-- Data for Name: match; Type: TABLE DATA; Schema: public; Owner: vagrant
--

INSERT INTO match VALUES (1, 1, 2, 1, '2014-12-10', 0);
INSERT INTO match VALUES (2, 2, 3, 2, '2015-10-12', 0);
INSERT INTO match VALUES (3, 3, 4, 4, '2015-10-31', 0);


--
-- Name: match_objectid_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('match_objectid_seq', 3, true);


--
-- Data for Name: player; Type: TABLE DATA; Schema: public; Owner: vagrant
--

INSERT INTO player VALUES (1, 'Neslihan', 'Darnel', '1983-12-09', 187, 72, '1995-03-12', 5, 3, 2, 3, 1, 17, 0);
INSERT INTO player VALUES (2, 'Nadia', 'Centoni', '1981-06-19', 185, 63, '1998-01-01', 1, 8, 2, 3, 2, 13, 0);
INSERT INTO player VALUES (3, 'Merve', 'Dalbeler', '1987-06-27', 180, 70, '2005-01-01', 2, 3, 2, 6, 1, 2, 0);


--
-- Name: player_objectid_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('player_objectid_seq', 3, true);


--
-- Data for Name: position; Type: TABLE DATA; Schema: public; Owner: vagrant
--

INSERT INTO "position" VALUES (1, 'Right Back', 0);
INSERT INTO "position" VALUES (2, 'Right Front', 0);
INSERT INTO "position" VALUES (3, 'Middle Front', 0);
INSERT INTO "position" VALUES (4, 'Left Front', 0);
INSERT INTO "position" VALUES (5, 'Left Back', 0);
INSERT INTO "position" VALUES (6, 'Middle Back', 0);


--
-- Name: position_objectid_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('position_objectid_seq', 6, true);


--
-- Data for Name: season; Type: TABLE DATA; Schema: public; Owner: vagrant
--

INSERT INTO season VALUES (1, '2011-2012', 0);
INSERT INTO season VALUES (2, '2012-2013', 0);
INSERT INTO season VALUES (3, '2013-2014', 0);
INSERT INTO season VALUES (4, '2014-2015', 0);


--
-- Name: season_objectid_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('season_objectid_seq', 4, true);


--
-- Data for Name: statistic; Type: TABLE DATA; Schema: public; Owner: vagrant
--

INSERT INTO statistic VALUES (1, 188, 192, 170, 55, 2, 1, 0);
INSERT INTO statistic VALUES (2, 180, 195, 200, 25, 3, 3, 0);


--
-- Name: statistic_objectid_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('statistic_objectid_seq', 2, true);


--
-- Data for Name: team; Type: TABLE DATA; Schema: public; Owner: vagrant
--

INSERT INTO team VALUES (1, 'Galatasaray', 'Yellow-Red', '1905-10-01', 3, 1, 0);
INSERT INTO team VALUES (2, 'Fenerbahçe', 'Blue-Yellow', '1905-05-03', 3, 2, 0);
INSERT INTO team VALUES (3, 'Vakıfbank', 'Yellow-White', '1986-01-01', 3, 4, 0);
INSERT INTO team VALUES (4, 'Real Madrid', 'White', '1902-03-05', 5, 3, 0);
INSERT INTO team VALUES (5, 'Eczacıbaşı', 'Blue-White', '1966-03-05', 3, 5, 0);


--
-- Name: team_objectid_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('team_objectid_seq', 5, true);


--
-- Data for Name: transfer; Type: TABLE DATA; Schema: public; Owner: vagrant
--

INSERT INTO transfer VALUES (1, 1, 3, 5, 1, 0);
INSERT INTO transfer VALUES (2, 3, 1, 2, 3, 0);


--
-- Name: transfer_objectid_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('transfer_objectid_seq', 2, true);


--
-- Data for Name: userinformation; Type: TABLE DATA; Schema: public; Owner: vagrant
--



--
-- Name: userinformation_objectid_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('userinformation_objectid_seq', 1, false);


--
-- Data for Name: userrole; Type: TABLE DATA; Schema: public; Owner: vagrant
--



--
-- Name: userrole_objectid_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('userrole_objectid_seq', 1, false);


--
-- Data for Name: usertable; Type: TABLE DATA; Schema: public; Owner: vagrant
--



--
-- Name: usertable_objectid_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('usertable_objectid_seq', 1, false);


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
-- Name: coach_countryid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY coach
    ADD CONSTRAINT coach_countryid_fkey FOREIGN KEY (countryid) REFERENCES country(objectid) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: coach_genderid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY coach
    ADD CONSTRAINT coach_genderid_fkey FOREIGN KEY (genderid) REFERENCES gender(objectid) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: coach_teamid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY coach
    ADD CONSTRAINT coach_teamid_fkey FOREIGN KEY (teamid) REFERENCES team(objectid) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: match_awayteamid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY match
    ADD CONSTRAINT match_awayteamid_fkey FOREIGN KEY (awayteamid) REFERENCES team(objectid) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: match_courtid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY match
    ADD CONSTRAINT match_courtid_fkey FOREIGN KEY (courtid) REFERENCES court(objectid) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: match_hometeamid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY match
    ADD CONSTRAINT match_hometeamid_fkey FOREIGN KEY (hometeamid) REFERENCES team(objectid) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: player_countryid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY player
    ADD CONSTRAINT player_countryid_fkey FOREIGN KEY (countryid) REFERENCES country(objectid) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: player_genderid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY player
    ADD CONSTRAINT player_genderid_fkey FOREIGN KEY (genderid) REFERENCES gender(objectid) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: player_handid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY player
    ADD CONSTRAINT player_handid_fkey FOREIGN KEY (handid) REFERENCES hand(objectid) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: player_positionid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY player
    ADD CONSTRAINT player_positionid_fkey FOREIGN KEY (positionid) REFERENCES "position"(objectid) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: player_teamid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY player
    ADD CONSTRAINT player_teamid_fkey FOREIGN KEY (teamid) REFERENCES team(objectid) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: statistic_playerid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY statistic
    ADD CONSTRAINT statistic_playerid_fkey FOREIGN KEY (playerid) REFERENCES player(objectid) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: statistic_seasonid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY statistic
    ADD CONSTRAINT statistic_seasonid_fkey FOREIGN KEY (seasonid) REFERENCES season(objectid) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: team_countryid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY team
    ADD CONSTRAINT team_countryid_fkey FOREIGN KEY (countryid) REFERENCES country(objectid) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: team_courtid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY team
    ADD CONSTRAINT team_courtid_fkey FOREIGN KEY (courtid) REFERENCES court(objectid) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: transfer_newteamid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY transfer
    ADD CONSTRAINT transfer_newteamid_fkey FOREIGN KEY (newteamid) REFERENCES team(objectid) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: transfer_oldteamid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY transfer
    ADD CONSTRAINT transfer_oldteamid_fkey FOREIGN KEY (oldteamid) REFERENCES team(objectid) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: transfer_playerid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY transfer
    ADD CONSTRAINT transfer_playerid_fkey FOREIGN KEY (playerid) REFERENCES player(objectid) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: transfer_seasonid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY transfer
    ADD CONSTRAINT transfer_seasonid_fkey FOREIGN KEY (seasonid) REFERENCES season(objectid) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: userinformation_favoriteteamid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY userinformation
    ADD CONSTRAINT userinformation_favoriteteamid_fkey FOREIGN KEY (favoriteteamid) REFERENCES team(objectid) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: usertable_userinformationid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY usertable
    ADD CONSTRAINT usertable_userinformationid_fkey FOREIGN KEY (userinformationid) REFERENCES userinformation(objectid) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: usertable_userroleid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY usertable
    ADD CONSTRAINT usertable_userroleid_fkey FOREIGN KEY (userroleid) REFERENCES userrole(objectid) ON UPDATE CASCADE ON DELETE RESTRICT;


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

