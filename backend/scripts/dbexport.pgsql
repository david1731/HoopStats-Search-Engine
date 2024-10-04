--
-- PostgreSQL database dump
--

-- Dumped from database version 14.13 (Homebrew)
-- Dumped by pg_dump version 14.13 (Homebrew)

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

--
-- Name: app; Type: SCHEMA; Schema: -; Owner: davidmendez
--

CREATE SCHEMA app;


ALTER SCHEMA app OWNER TO davidmendez;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: games; Type: TABLE; Schema: public; Owner: okcapplicant
--

CREATE TABLE public.games (
    id integer NOT NULL,
    date date NOT NULL,
    home_team_id integer,
    away_team_id integer
);


ALTER TABLE public.games OWNER TO okcapplicant;

--
-- Name: games_id_seq; Type: SEQUENCE; Schema: public; Owner: okcapplicant
--

CREATE SEQUENCE public.games_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.games_id_seq OWNER TO okcapplicant;

--
-- Name: games_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: okcapplicant
--

ALTER SEQUENCE public.games_id_seq OWNED BY public.games.id;


--
-- Name: player_stats; Type: TABLE; Schema: public; Owner: okcapplicant
--

CREATE TABLE public.player_stats (
    id integer NOT NULL,
    game_id integer,
    player_id integer,
    team_id integer,
    is_starter boolean,
    minutes integer,
    points integer,
    assists integer,
    offensive_rebounds integer,
    defensive_rebounds integer,
    steals integer,
    blocks integer,
    turnovers integer,
    defensive_fouls integer,
    offensive_fouls integer
);


ALTER TABLE public.player_stats OWNER TO okcapplicant;

--
-- Name: player_stats_id_seq; Type: SEQUENCE; Schema: public; Owner: okcapplicant
--

CREATE SEQUENCE public.player_stats_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.player_stats_id_seq OWNER TO okcapplicant;

--
-- Name: player_stats_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: okcapplicant
--

ALTER SEQUENCE public.player_stats_id_seq OWNED BY public.player_stats.id;


--
-- Name: players; Type: TABLE; Schema: public; Owner: okcapplicant
--

CREATE TABLE public.players (
    id integer NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE public.players OWNER TO okcapplicant;

--
-- Name: players_id_seq; Type: SEQUENCE; Schema: public; Owner: okcapplicant
--

CREATE SEQUENCE public.players_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.players_id_seq OWNER TO okcapplicant;

--
-- Name: players_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: okcapplicant
--

ALTER SEQUENCE public.players_id_seq OWNED BY public.players.id;


--
-- Name: teams; Type: TABLE; Schema: public; Owner: okcapplicant
--

CREATE TABLE public.teams (
    id integer NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE public.teams OWNER TO okcapplicant;

--
-- Name: teams_id_seq; Type: SEQUENCE; Schema: public; Owner: okcapplicant
--

CREATE SEQUENCE public.teams_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.teams_id_seq OWNER TO okcapplicant;

--
-- Name: teams_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: okcapplicant
--

ALTER SEQUENCE public.teams_id_seq OWNED BY public.teams.id;


--
-- Name: games id; Type: DEFAULT; Schema: public; Owner: okcapplicant
--

ALTER TABLE ONLY public.games ALTER COLUMN id SET DEFAULT nextval('public.games_id_seq'::regclass);


--
-- Name: player_stats id; Type: DEFAULT; Schema: public; Owner: okcapplicant
--

ALTER TABLE ONLY public.player_stats ALTER COLUMN id SET DEFAULT nextval('public.player_stats_id_seq'::regclass);


--
-- Name: players id; Type: DEFAULT; Schema: public; Owner: okcapplicant
--

ALTER TABLE ONLY public.players ALTER COLUMN id SET DEFAULT nextval('public.players_id_seq'::regclass);


--
-- Name: teams id; Type: DEFAULT; Schema: public; Owner: okcapplicant
--

ALTER TABLE ONLY public.teams ALTER COLUMN id SET DEFAULT nextval('public.teams_id_seq'::regclass);


--
-- Data for Name: games; Type: TABLE DATA; Schema: public; Owner: okcapplicant
--

COPY public.games (id, date, home_team_id, away_team_id) FROM stdin;
1	2022-12-19	1	2
2	2022-12-21	1	2
3	2023-02-10	2	1
4	2023-03-26	2	1
\.


--
-- Data for Name: player_stats; Type: TABLE DATA; Schema: public; Owner: okcapplicant
--

COPY public.player_stats (id, game_id, player_id, team_id, is_starter, minutes, points, assists, offensive_rebounds, defensive_rebounds, steals, blocks, turnovers, defensive_fouls, offensive_fouls) FROM stdin;
325	1	17	1	f	16	12	1	0	3	0	1	0	1	0
326	1	18	1	t	35	35	6	0	2	1	2	2	2	0
327	1	19	1	f	28	12	2	1	3	2	0	2	2	1
328	1	20	1	t	31	13	0	2	1	1	0	2	4	1
329	1	21	1	t	23	8	3	3	3	0	1	2	2	0
330	1	22	1	f	23	11	1	0	3	1	0	0	1	0
331	1	23	1	f	10	1	1	0	1	0	0	0	1	0
332	1	27	1	t	25	12	1	2	2	1	0	0	2	0
333	1	28	1	f	12	6	1	1	5	0	0	1	2	0
334	1	29	1	t	33	13	4	2	5	1	1	1	2	0
335	1	15	2	f	10	6	0	1	2	0	0	0	0	0
336	1	1	2	t	38	28	6	0	3	1	0	4	4	0
337	1	2	2	t	41	26	3	3	5	2	0	4	0	2
338	1	4	2	f	22	8	2	4	2	1	0	2	4	1
339	1	6	2	t	32	13	6	2	6	0	0	0	2	0
340	1	8	2	t	34	19	1	0	4	1	0	2	5	0
341	1	9	2	t	31	9	3	2	5	0	2	0	4	0
342	1	13	2	f	13	9	1	2	2	0	0	0	1	0
343	1	14	2	f	14	3	4	0	2	0	0	4	2	3
344	2	22	1	f	17	6	1	0	2	1	0	0	2	0
345	2	23	1	f	6	3	1	1	0	0	0	0	0	0
346	2	26	1	t	30	13	6	2	4	1	0	3	0	0
347	2	27	1	f	9	0	0	1	2	0	0	1	0	1
348	2	29	1	t	30	15	1	0	4	0	0	3	2	0
349	2	17	1	f	20	6	0	0	1	0	1	0	5	0
350	2	18	1	t	35	27	3	0	6	2	1	5	1	2
351	2	19	1	f	26	9	2	4	3	2	0	1	0	0
352	2	20	1	t	38	14	3	0	3	1	1	3	2	0
353	2	21	1	t	19	6	2	1	2	2	0	1	1	0
354	2	28	1	f	3	2	0	0	1	0	0	1	0	0
355	2	14	2	f	18	8	1	2	5	1	0	1	2	1
356	2	1	2	t	36	16	8	0	2	2	0	4	2	0
357	2	3	2	t	22	12	4	1	5	1	0	1	1	0
358	2	4	2	f	15	3	2	1	1	0	1	0	0	0
359	2	6	2	t	34	13	2	1	4	1	0	5	3	2
360	2	8	2	t	29	12	4	0	1	1	1	3	3	2
361	2	9	2	f	19	6	3	4	3	3	1	1	2	0
362	2	13	2	f	7	3	1	0	0	0	1	1	2	0
363	2	15	2	f	19	8	0	0	1	0	0	0	0	0
364	2	2	2	t	35	17	4	0	5	0	1	2	2	0
365	3	14	2	f	16	4	3	1	1	0	0	0	5	0
366	3	10	2	t	17	11	2	0	2	0	0	0	3	0
367	3	11	2	f	24	8	1	2	3	0	1	3	2	1
368	3	1	2	t	35	38	9	1	1	1	0	6	2	1
369	3	16	2	f	13	10	1	1	2	0	0	1	1	1
370	3	15	2	f	28	13	3	1	2	1	2	0	0	0
371	3	2	2	t	36	23	2	0	4	0	1	4	5	0
372	3	9	2	t	28	9	2	2	6	0	1	2	2	1
373	3	8	2	t	36	11	6	1	2	1	0	2	2	0
374	3	13	2	f	1	2	0	0	0	0	0	0	1	0
375	3	22	1	f	23	12	3	0	3	0	0	1	1	0
376	3	30	1	f	18	11	1	1	1	0	0	0	3	0
377	3	25	1	f	20	9	3	1	0	1	1	2	0	0
378	3	27	1	t	20	2	1	2	2	0	0	1	4	1
379	3	23	1	f	3	0	0	0	0	0	0	0	0	0
380	3	18	1	t	39	44	7	0	3	2	1	4	1	0
381	3	28	1	f	7	2	0	1	1	0	0	1	1	1
382	3	26	1	t	28	19	7	3	3	0	0	0	4	0
383	3	29	1	t	32	13	6	1	3	3	0	1	2	1
384	3	20	1	f	20	18	1	1	0	1	1	0	5	0
385	3	19	1	t	26	8	0	0	3	2	0	0	2	0
386	4	14	2	t	10	6	0	0	2	0	0	2	0	0
387	4	16	2	f	14	2	0	2	0	1	1	0	2	0
388	4	11	2	f	31	28	0	2	4	0	0	2	4	1
389	4	13	2	f	21	14	5	1	0	0	0	3	1	0
390	4	7	2	f	15	11	0	1	4	0	0	0	3	0
391	4	5	2	t	26	3	5	0	2	0	0	1	2	0
392	4	9	2	t	32	7	4	2	8	1	6	3	1	1
393	4	10	2	f	19	4	0	0	0	1	0	1	1	0
394	4	15	2	t	35	29	3	0	5	0	0	5	3	0
395	4	12	2	t	32	8	1	0	4	2	0	1	2	1
396	4	31	1	f	12	4	0	1	0	1	0	1	1	0
397	4	24	1	f	13	5	0	0	1	1	0	0	2	0
398	4	25	1	f	14	5	2	1	1	0	0	0	3	0
399	4	27	1	f	7	0	0	0	1	0	0	1	1	1
400	4	22	1	f	28	20	5	2	5	2	0	0	2	0
401	4	18	1	t	35	31	3	2	0	4	0	3	1	0
402	4	26	1	t	35	17	6	1	10	1	2	2	0	0
403	4	29	1	t	37	23	4	1	4	2	0	1	1	0
404	4	30	1	t	26	7	2	2	4	0	0	1	3	0
405	4	20	1	t	28	6	1	3	3	2	0	2	4	0
\.


--
-- Data for Name: players; Type: TABLE DATA; Schema: public; Owner: okcapplicant
--

COPY public.players (id, name) FROM stdin;
1	Michael Jordan
2	Tweety
3	Bugs Bunny
4	Daffy Duck
5	Sniffles
6	Yosemite Sam
7	Road Runner
8	Porky Pig
9	Sylvester
10	Lola Bunny
11	Wile E. Coyote
12	Bill Murray
13	Barnyard Dawg
14	Tasmanian Devil
15	Foghorn Leghorn
16	Elmer Fudd
17	Monstar 1
18	Monstar 2
19	Monstar 3
20	Monstar 4
21	Monstar 5
22	Monstar 6
23	Monstar 7
24	Monstar 8
25	Monstar 9
26	Monstar 10
27	Monstar 11
28	Monstar 12
29	Monstar 13
30	Monstar 14
31	Monstar 15
\.


--
-- Data for Name: teams; Type: TABLE DATA; Schema: public; Owner: okcapplicant
--

COPY public.teams (id, name) FROM stdin;
1	Tune Squad
2	Monstars
\.


--
-- Name: games_id_seq; Type: SEQUENCE SET; Schema: public; Owner: okcapplicant
--

SELECT pg_catalog.setval('public.games_id_seq', 1, false);


--
-- Name: player_stats_id_seq; Type: SEQUENCE SET; Schema: public; Owner: okcapplicant
--

SELECT pg_catalog.setval('public.player_stats_id_seq', 486, true);


--
-- Name: players_id_seq; Type: SEQUENCE SET; Schema: public; Owner: okcapplicant
--

SELECT pg_catalog.setval('public.players_id_seq', 1, false);


--
-- Name: teams_id_seq; Type: SEQUENCE SET; Schema: public; Owner: okcapplicant
--

SELECT pg_catalog.setval('public.teams_id_seq', 1, false);


--
-- Name: games games_pkey; Type: CONSTRAINT; Schema: public; Owner: okcapplicant
--

ALTER TABLE ONLY public.games
    ADD CONSTRAINT games_pkey PRIMARY KEY (id);


--
-- Name: player_stats player_stats_pkey; Type: CONSTRAINT; Schema: public; Owner: okcapplicant
--

ALTER TABLE ONLY public.player_stats
    ADD CONSTRAINT player_stats_pkey PRIMARY KEY (id);


--
-- Name: players players_pkey; Type: CONSTRAINT; Schema: public; Owner: okcapplicant
--

ALTER TABLE ONLY public.players
    ADD CONSTRAINT players_pkey PRIMARY KEY (id);


--
-- Name: teams teams_pkey; Type: CONSTRAINT; Schema: public; Owner: okcapplicant
--

ALTER TABLE ONLY public.teams
    ADD CONSTRAINT teams_pkey PRIMARY KEY (id);


--
-- Name: player_stats unique_game_player; Type: CONSTRAINT; Schema: public; Owner: okcapplicant
--

ALTER TABLE ONLY public.player_stats
    ADD CONSTRAINT unique_game_player UNIQUE (game_id, player_id);


--
-- Name: games games_away_team_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: okcapplicant
--

ALTER TABLE ONLY public.games
    ADD CONSTRAINT games_away_team_id_fkey FOREIGN KEY (away_team_id) REFERENCES public.teams(id);


--
-- Name: games games_home_team_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: okcapplicant
--

ALTER TABLE ONLY public.games
    ADD CONSTRAINT games_home_team_id_fkey FOREIGN KEY (home_team_id) REFERENCES public.teams(id);


--
-- Name: player_stats player_stats_game_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: okcapplicant
--

ALTER TABLE ONLY public.player_stats
    ADD CONSTRAINT player_stats_game_id_fkey FOREIGN KEY (game_id) REFERENCES public.games(id);


--
-- Name: player_stats player_stats_player_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: okcapplicant
--

ALTER TABLE ONLY public.player_stats
    ADD CONSTRAINT player_stats_player_id_fkey FOREIGN KEY (player_id) REFERENCES public.players(id);


--
-- Name: player_stats player_stats_team_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: okcapplicant
--

ALTER TABLE ONLY public.player_stats
    ADD CONSTRAINT player_stats_team_id_fkey FOREIGN KEY (team_id) REFERENCES public.teams(id);


--
-- Name: SCHEMA app; Type: ACL; Schema: -; Owner: davidmendez
--

GRANT ALL ON SCHEMA app TO okcapplicant;


--
-- PostgreSQL database dump complete
--

