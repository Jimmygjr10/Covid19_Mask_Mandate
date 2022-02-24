--
-- PostgreSQL database dump
--

-- Dumped from database version 13.4
-- Dumped by pg_dump version 13.4

-- Started on 2022-02-19 10:07:34

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

DROP DATABASE "COVID";
--
-- TOC entry 2995 (class 1262 OID 17522)
-- Name: COVID; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE "COVID" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';


ALTER DATABASE "COVID" OWNER TO postgres;

\connect "COVID"

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
-- TOC entry 202 (class 1259 OID 17830)
-- Name: county_pop_loc_sqlmerge; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.county_pop_loc_sqlmerge (
    state_fips double precision,
    state_name_x text,
    fips bigint,
    county_name_x text,
    mask_mandate bigint,
    month_started bigint,
    mandate_duration_months bigint,
    date text,
    county text,
    state text,
    cases bigint,
    deaths bigint,
    popestimate2020 integer,
    lat double precision,
    lng double precision
);


ALTER TABLE public.county_pop_loc_sqlmerge OWNER TO postgres;

--
-- TOC entry 201 (class 1259 OID 17820)
-- Name: fmdll; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fmdll (
    index bigint,
    state_fips double precision,
    state_name_x text,
    fips bigint,
    county_name_x text,
    county_start_date timestamp without time zone,
    county_end_date text,
    state_start_date text,
    state_end_date text,
    earliest_start_date text,
    mask_mandate bigint,
    month_started bigint,
    mandate_duration_months bigint,
    date text,
    county text,
    state text,
    cases bigint,
    deaths bigint,
    county_name_y text,
    state_name_y text,
    lat double precision,
    lng double precision
);


ALTER TABLE public.fmdll OWNER TO postgres;

--
-- TOC entry 200 (class 1259 OID 17641)
-- Name: pt; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pt (
    "SUMLEV" integer,
    "REGION" integer,
    "DIVISION" integer,
    "STATE" integer,
    "COUNTY" integer,
    fips integer,
    "STNAME" character varying,
    "CTYNAME" character varying,
    "CENSUS2010POP" integer,
    "ESTIMATESBASE2010" integer,
    "POPESTIMATE2010" integer,
    "POPESTIMATE2011" integer,
    "POPESTIMATE2012" integer,
    "POPESTIMATE2013" integer,
    "POPESTIMATE2014" integer,
    "POPESTIMATE2015" integer,
    "POPESTIMATE2016" integer,
    "POPESTIMATE2017" integer,
    "POPESTIMATE2018" integer,
    "POPESTIMATE2019" integer,
    "POPESTIMATE042020" integer,
    popestimate2020 integer
);


ALTER TABLE public.pt OWNER TO postgres;

--
-- TOC entry 2859 (class 1259 OID 17826)
-- Name: ix_fmdll_index; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_fmdll_index ON public.fmdll USING btree (index);


-- Completed on 2022-02-19 10:07:35

--
-- PostgreSQL database dump complete
--

