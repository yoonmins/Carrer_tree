CREATE TABLE `carr`.`carr_tree` (
  `no` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `position` VARCHAR(45) NOT NULL,
  `summary` TEXT NOT NULL,
  `photo` BLOB NULL,
  `link` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`no`))
COMMENT = '이력서';


select * from carr.carr_tree;

INSERT INTO carr.carr_tree (name, position, summary, photo, link)
VALUES ('문우형', 'backend', 'df', NULL, 'ht');