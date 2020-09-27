CREATE TABLE `user`
(
    `id`              int PRIMARY KEY AUTO_INCREMENT,
    `url`             varchar(128) NOT NULL UNIQUE,
    `name`            text,
    `gender`          int,
    `follower`        bigint,
    `deleted`         boolean,
    `updatetimestamp` timestamp,
    `createtimestamp` timestamp,
    `deletetimestamp` timestamp    NULL DEFAULT NULL
);

CREATE TABLE `job`
(
    `id`              int PRIMARY KEY AUTO_INCREMENT,
    `company`         varchar(128) NOT NULL UNIQUE,
    `position`        text,
    `updatetimestamp` timestamp,
    `createtimestamp` timestamp,
    `deletetimestamp` timestamp    NULL DEFAULT NULL
);

CREATE TABLE `education`
(
    `id`              int PRIMARY KEY AUTO_INCREMENT,
    `school`          varchar(128) NOT NULL UNIQUE,
    `degree`          int,
    `updatetimestamp` timestamp,
    `createtimestamp` timestamp,
    `deletetimestamp` timestamp    NULL DEFAULT NULL
);

CREATE TABLE `location`
(
    `id`              int PRIMARY KEY AUTO_INCREMENT,
    `location`        varchar(128) NOT NULL UNIQUE,
    `updatetimestamp` timestamp,
    `createtimestamp` timestamp,
    `deletetimestamp` timestamp    NULL DEFAULT NULL
);

CREATE TABLE `userjob`
(
    `id`              int PRIMARY KEY AUTO_INCREMENT,
    `userid`          int,
    `jobid`           int,
    `jobstart`        timestamp,
    `jobend`          timestamp,
    `createtimestamp` timestamp,
    `deletetimestamp` timestamp NULL DEFAULT NULL
);

ALTER TABLE userjob
    ADD CONSTRAINT UNIQUE_LINK UNIQUE CLUSTERED (userid, jobid);

CREATE TABLE `userlocation`
(
    `id`              int PRIMARY KEY AUTO_INCREMENT,
    `userid`          int,
    `locationid`      int,
    `createtimestamp` timestamp,
    `deletetimestamp` timestamp NULL DEFAULT NULL
);

ALTER TABLE userlocation
    ADD CONSTRAINT UNIQUE_LINK UNIQUE CLUSTERED (userid, locationid);

CREATE TABLE `usereducation`
(
    `id`              int PRIMARY KEY AUTO_INCREMENT,
    `userid`          int,
    `educationid`     int,
    `createtimestamp` timestamp,
    `deletetimestamp` timestamp NULL DEFAULT NULL
);


ALTER TABLE usereducation
    ADD CONSTRAINT UNIQUE_LINK UNIQUE CLUSTERED (userid, educationid);

CREATE TABLE `fanpage`
(
    `id`              int PRIMARY KEY AUTO_INCREMENT,
    `url`             varchar(128) NOT NULL UNIQUE,
    `type`            text,
    `name`            text,
    `like`            bigint,
    `follower`        bigint,
    `deleted`         boolean,
    `updatetimestamp` timestamp,
    `createtimestamp` timestamp,
    `deletetimestamp` timestamp    NULL DEFAULT NULL
);

CREATE TABLE `target_fanpage`
(
    `id`     int PRIMARY KEY AUTO_INCREMENT,
    `url`    varchar(128) NOT NULL UNIQUE,
    `option` text
);

CREATE TABLE `userinterest`
(
    `id`              int PRIMARY KEY AUTO_INCREMENT,
    `userid`          int,
    `fanpageid`       int,
    `createtimestamp` timestamp,
    `deletetimestamp` timestamp NULL DEFAULT NULL
);

ALTER TABLE userinterest
    ADD CONSTRAINT UNIQUE_LINK UNIQUE CLUSTERED (userid, fanpageid);

CREATE TABLE `post`
(
    `id`              int PRIMARY KEY AUTO_INCREMENT,
    `url`             varchar(128) NOT NULL UNIQUE,
    `type`            text,
    `content`         text,
    `likes`           int,
    `heart`           int,
    `angry`           int,
    `wow`             int,
    `haha`            int,
    `cry`             int,
    `updatetimestamp` timestamp,
    `createtimestamp` timestamp,
    `deletetimestamp` timestamp    NULL DEFAULT NULL,
    `posttimestamp`   timestamp
);

CREATE TABLE `postemoji`
(
    `id`              int PRIMARY KEY AUTO_INCREMENT,
    `postid`          int,
    `userid`          int,
    `likes`           boolean,
    `heart`           boolean,
    `angry`           boolean,
    `wow`             boolean,
    `haha`            boolean,
    `cry`             boolean,
    `updatetimestamp` timestamp,
    `createtimestamp` timestamp,
    `deletetimestamp` timestamp NULL DEFAULT NULL
);

CREATE TABLE `userpost`
(
    `id`              int PRIMARY KEY AUTO_INCREMENT,
    `userid`          int,
    `postid`          int,
    `emoji`           int,
    `deleted`         boolean,
    `updatetimestamp` timestamp,
    `createtimestamp` timestamp,
    `deletetimestamp` timestamp NULL DEFAULT NULL
);

ALTER TABLE userpost
    ADD CONSTRAINT UNIQUE_LINK UNIQUE CLUSTERED (userid, postid);

CREATE TABLE `fanpagepost`
(
    `id`              int PRIMARY KEY AUTO_INCREMENT,
    `fanpageid`       int,
    `postid`          int,
    `deleted`         boolean,
    `updatetimestamp` timestamp,
    `createtimestamp` timestamp,
    `deletetimestamp` timestamp NULL DEFAULT NULL
);


ALTER TABLE fanpagepost
    ADD CONSTRAINT UNIQUE_LINK UNIQUE CLUSTERED (fanpageid, postid);


CREATE TABLE `task_error`
(
    `id`              int PRIMARY KEY AUTO_INCREMENT,
    `task_id`         varchar(20) NOT NULL UNIQUE,
    `machine_id`      varchar(20),
    `url`             varchar(256),
    `exec_cmd`        varchar(40),
    `error_type`      text,
    `trace_back`      text,
    `html`            text,
    `time`            timestamp        DEFAULT CURRENT_TIMESTAMP,
    `deletetimestamp` timestamp   NULL DEFAULT NULL
);

CREATE VIEW fanpage_degree AS
SELECT a.id, a.url, a.name, b.count_link
FROM `fanpage` as a,
     (SELECT `fanpageid`, COUNT(`userid`) as `count_link` FROM `userinterest` GROUP BY `fanpageid`) as b
WHERE a.id = b.fanpageid
ORDER BY `b`.`count_link` DESC;

CREATE VIEW todo_fanpage AS
SELECT a.url, a.id, a.name, a.like, b.count_link
FROM `fanpage` as a,
     (SELECT `fanpageid`, COUNT(`userid`) as `count_link` FROM `userinterest` GROUP BY `fanpageid`) as b
WHERE a.id = b.fanpageid
  AND a.`like` IS NOT NULL
ORDER BY `b`.`count_link` DESC;

CREATE VIEW todo_user AS
SELECT a.url, a.id, a.name
FROM `user` as a
WHERE a.name IS NULL
  AND a.deleted IS NULL;

CREATE VIEW todo_post AS
SELECT `post`.id, `post`.url, `post`.`type`
FROM `post`
WHERE `post`.id NOT IN
      (SELECT a.id
       FROM `post` as a,
            (SELECT `postid`, COUNT(`userid`) as `count_link` FROM `userpost` GROUP BY `postid`) as b
       WHERE a.id = b.postid
         and b.count_link > 0
      );

ALTER TABLE `userinterest`
    ADD FOREIGN KEY (`userid`) REFERENCES `user` (`id`);

ALTER TABLE `userinterest`
    ADD FOREIGN KEY (`fanpageid`) REFERENCES `fanpage` (`id`);

ALTER TABLE `userpost`
    ADD FOREIGN KEY (`userid`) REFERENCES `user` (`id`);

ALTER TABLE `userpost`
    ADD FOREIGN KEY (`postid`) REFERENCES `post` (`id`);

ALTER TABLE `fanpagepost`
    ADD FOREIGN KEY (`fanpageid`) REFERENCES `fanpage` (`id`);

ALTER TABLE `fanpagepost`
    ADD FOREIGN KEY (`postid`) REFERENCES `post` (`id`);

ALTER TABLE `postemoji`
    ADD FOREIGN KEY (`postid`) REFERENCES `post` (`id`);

ALTER TABLE `usereducation`
    ADD FOREIGN KEY (`userid`) REFERENCES `user` (`id`);

ALTER TABLE `usereducation`
    ADD FOREIGN KEY (`educationid`) REFERENCES `education` (`id`);

ALTER TABLE `userlocation`
    ADD FOREIGN KEY (`userid`) REFERENCES `user` (`id`);

ALTER TABLE `userlocation`
    ADD FOREIGN KEY (`locationid`) REFERENCES `location` (`id`);

ALTER TABLE `userjob`
    ADD FOREIGN KEY (`userid`) REFERENCES `user` (`id`);

ALTER TABLE `userjob`
    ADD FOREIGN KEY (`jobid`) REFERENCES `job` (`id`);


