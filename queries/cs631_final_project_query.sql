CREATE TABLE `cs631_db`.`employees` (
  `employee_id` INT NOT NULL AUTO_INCREMENT,
  `category_id` INT NULL,
  `employee_name` VARCHAR(150) NULL,
  `employee_email` VARCHAR(70) NULL,
  `employee_poistion` VARCHAR(45) NULL,
  `employee_office` VARCHAR(45) NULL,
  `employee_phone` INT(10) NULL,
  `employee_salary` INT(10) NULL,
  PRIMARY KEY (`employee_id`));
