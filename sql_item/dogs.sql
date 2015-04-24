/*              InstDogsLogin.SQL - Creates the Dogs Login database         */ 

SET NOCOUNT ON -- won't print how many record(s) it processed on the screen.
GO	--Stop here until completed.

USE master	--Database of databases.

declare @dttm varchar(55)	--Here we go.
select  @dttm=convert(varchar,getdate(),113)
raiserror('Beginning InstDogsLogin.SQL at %s ....',1,1,@dttm) with nowait --Not really an error but rather a comment printed to the screen.

GO	--Stop here until completed.

if exists (select * from sysdatabases where name='DogsLogin') begin	--if an outdated database already exists then...
  raiserror('Dropping existing Dogs Login database ....',0,1)
  ALTER DATABASE DogsLogin SET  SINGLE_USER WITH ROLLBACK IMMEDIATE	--avoids errors in some versions of MSSQL
  DROP database DogsLogin
end
GO	--Stop here until...

--CHECKPOINT
go

raiserror('Creating DogsLogin database....',0,1)	--printable comment.
go

/* Use a default size with autogrow */

CREATE DATABASE DogsLogin
GO		

--CHECKPOINT

GO

USE DogsLogin

GO

if db_name() <> 'DogsLogin'	-- then oops.
   raiserror('Error in InstDogsLogin.SQL, ''USE DogsLogin'' failed!  Killing the SPID now.',22,127) with log
GO

--execute sp_dboption 'DogsLogin' ,'trunc. log on chkpt.' ,'true'
GO

/*tables*/

CREATE TABLE tUser(  --  drop table tUser
  iUserKey				int				NOT NULL PRIMARY KEY CLUSTERED,				--Primary index is the data in a B- tree format.
  acName				varchar(32)		NOT NULL CHECK (acName <> ''),				--Login Name.
  abPassword			varBinary(32)	NOT NULL CHECK (abPassword <> ''),			--Case sensitive password.
  acEmail				varchar(256)	NOT NULL CHECK (acEMail <> ''),				--Point of contact
  acSecurityQuestion	varchar(256)	NOT NULL CHECK (acSecurityQuestion <> ''),	--Let them pick their own question.
  acSecurityAnswer		varchar(256)	NOT NULL CHECK (acSecurityAnswer <> '')		--Let them pick their own answer.
)
GO

/*	Highlight and execute the following to test an input.
INSERT INTO tUser (iUserKey, acName, abPassword, acEmail, acSecurityQuestion, acSecurityAnswer)
 VALUES (123, 'John Smith', CONVERT(varbinary, 'Secreto'), 'email@email.com', 'PotAto','PotaTo')
*/
GO
CREATE TABLE tUserHistory( --- drop table tUserhistory					--Highlight and execute to drop the table.
  ID				int				NOT NULL IDENTITY(1,10),
  iUserKey			int				NOT NULL FOREIGN KEY REFERENCES tUser(iUserKey),
  datNow			smalldatetime	NOT NULL DEFAULT GETUTCDATE(),		--Data may be gathered all over the globe and this will synchronize it if no date is included.
  iIsLogin			int				NOT NULL							--Type of login.
)
GO

--For security purposes, INSERT, UPDATE, and SELECT are done through stored procedures and views; no outside entity has direct access to the tables. Aso makes it easier to abstract the table to the outside world.

CREATE PROCEDURE pLogin -- DROP PROCEDURE pLogin	
  @acName		varchar(32),
  @acPassword	varchar(32)
AS
	Declare @iUserKey int
	SELECT @iUserKey = (SELECT TOP 1 iUserKey FROM tUser WHERE acName=@acName AND abPassword=CONVERT(varbinary,@acPassword)) --Password is case Sensitive.
  IF @@ROWCOUNT <> 0  BEGIN
	INSERT INTO tUserHistory (iUserKey, iIsLogin) VALUES (@iUserKey, -1)
	SELECT 1		--Valid Username and password.
  END ELSE BEGIN
	SELECT 0		--Invalid Username or password.
  END
GO

--Changing a password.
CREATE PROCEDURE pPasswordNew  -- drop procedure ppasswordnew
  @acName varchar(32),
  @acPassword varchar(32),
  @acPasswordNew varchar(32),
  @acConfirm varchar(32),
  @acNameNew varchar(32)
AS
  IF @acPasswordNew<>@acConfirm	--New password must match.
	SELECT 0		--Failed.
  ELSE
    BEGIN
      UPDATE tUser set abPassword = CONVERT(varbinary,@acPasswordNew), acName = @acNameNew WHERE acName=@acName AND abPassword=CONVERT(varbinary,@acPassword)
      IF @@ERROR=0 AND @@ROWCOUNT=1
	    SELECT 1	--Updated.
      ELSE
	    SELECT 0	--failed to update.
	END
GO
--execute pPasswordNew 'John Smith','Secreto', 'Secreto','Secreto', 'Jane Smith'

raiserror('Done DogsLogin database....',0,1)
GO
--CHECKPOINT
GO

--CREATE PROCEDURE uspUserInsert
--  @intID				int,
--  @acName				varchar(32),
--  @abPassword			varBinary(32),
--  @acEmail				varchar(256),
--  @acSecurityQuestion	varchar(256),
--  @acSecurityAnswer		varchar(256)
--AS
--  SET NOCOUNT ON
--  DECLARE @intRowCount integer,
--          @vchError varchar(2000),
--          @vchHistory varchar(7000),
--          --@myintID integer
  
--  IF EXISTS (SELECT * FROM tUser WHERE intID=@intID)	--Already exists so update the information.
--    BEGIN
--      UPDATE datCompany
--        SET intCompanyKey=@intCompanyKey, intParent=@intParent, vchName=@vchName, intStatus=@intStatus, intBilling=@intBilling
--        WHERE intCompanyKey=@intCompanyKey
--      SELECT @intRowCount = @@RowCount
--      IF @intRowCount = 0
--        BEGIN
--          SELECT @vchError = 'datCompany Update 0 count ' + convert(varchar(40), getdate()) + ' ' + convert(varchar(20),@intCompanyKey)
--          RAISERROR (@vchError, 16, 1) WITH LOG
--        END
--    END
--  ELSE													--New login.
--    BEGIN
--      EXECUTE pNextNumber @intCompanyKey OUTPUT	--Identity has flaws under heavy multiuse. Use the stored procedure instead.
--      EXECUTE pNextNumber @intHistoryKey OUTPUT	--Identity has flaws under heavy multiuse. Use the stored procedure instead.
--      SELECT @vchHistory = Convert(varchar(7000), @intCompanyKey) + Convert(varchar(7000), @intParent) + @vchName + Convert(varchar(7000), @intStatus) + Convert(varchar(7000), @intBilling)
--      INSERT INTO datHistory (intHistoryKey, intForeignKey, vchHistory) VALUES (@intHistoryKey, @intCompanyKey, @vchHistory)
--      SELECT @intRowCount = @@RowCount
--      IF @intRowCount = 0
--        BEGIN
--          SELECT @vchError = 'History Insert 0 count ' + convert(varchar(40), getdate()) + ' ' + convert(varchar(20),@intHistoryKey) + @vchHistory
--          RAISERROR (@vchError, 16, 1) WITH LOG
--        END
--      INSERT INTO datCompany (intCompanyKey, intParent, vchName, intStatus, intBilling)
--        VALUES (@intCompanyKey, @intParent, @vchName, @intStatus, @intBilling)
--      SELECT @intRowCount = @@RowCount
--      IF @intRowCount = 0
--        BEGIN
--          SELECT @vchError = 'datCompany Insert 0 count ' + convert(varchar(40), getdate()) + ' ' + convert(varchar(20),@intCompanyKey)
--          RAISERROR (@vchError, 16, 1) WITH LOG
--        END
--    END
--  SELECT @intCompanyKey AS intCompanyKey
--  SET NOCOUNT OFF
--RETURN @intRowCount
--GO





--/*              InstDogsAccount.SQL - Creates the Dogs Login database         */ 

--SET NOCOUNT ON
--GO

USE master

declare @dttm varchar(55)
select  @dttm=convert(varchar,getdate(),113)
raiserror('Beginning InstDogsAccount.SQL at %s ....',1,1,@dttm) with nowait

GO

USE MASTER
GO
if exists (select * from sysdatabases where name='DogsData') begin
  raiserror('Dropping existing Dogs Data database ....',0,1)
  ALTER DATABASE DogsData SET  SINGLE_USER WITH ROLLBACK IMMEDIATE	--avoids errors in some versions of MSSQL
  DROP database DogsData
end
GO

--CHECKPOINT
go

raiserror('Creating DogsData database....',0,1)
go

/* Use default size with autogrow */

CREATE DATABASE DogsData
GO

--CHECKPOINT

GO

USE DogsData

GO

if db_name() <> 'DogsData'
   raiserror('Error in InstDogsData.SQL, ''USE DogsData'' failed!  Killing the SPID now.',22,127) with log
GO

--execute sp_dboption 'DogsData' ,'trunc. log on chkpt.' ,'true'
GO

/*tables*/

CREATE TABLE tDepartment(	--	drop table tdepartment
  iDepartmentKey		int				NOT NULL PRIMARY KEY CLUSTERED IDENTITY(1,10),				--Primary index is the data in a B- tree format.
  acName				varchar(32)		NOT NULL CHECK (acName <> ''),				--They may have multiple departments.
  iDepartmentNumber		int				NOT NULL CHECK (iDepartmentNumber >= 0) UNIQUE
)
GO

CREATE TABLE tType(			--	drop table ttype
  iTypeKey				int				NOT NULL PRIMARY KEY CLUSTERED IDENTITY(2,10),				--Primary index is the data in a B- tree format.
  acName				varchar(32)		NOT NULL CHECK (acName <> ''),				--Types of gatherable data.
  iTypeNumber			int				NOT NULL CHECK (iTypeNumber >= 0) UNIQUE
)
GO

CREATE TABLE tUnit(			--	drop table tunit
  iUnitKey				int				NOT NULL PRIMARY KEY CLUSTERED IDENTITY(3,10),				--Primary index is the data in a B- tree format.
  iDepartmentKey		int				NOT NULL FOREIGN KEY REFERENCES tDepartment(iDepartmentKey),
  acName				varchar(32)		NOT NULL CHECK (acName <> ''),				--Data gathering machines on the cloud.
  iUnitNumber			int				NOT NULL CHECK (iUnitNumber >= 0) UNIQUE
)
GO

--CREATE TABLE tTypeUnit(		--	drop table ttypeunit
--  iTypeUnitKey			int				NOT NULL UNIQUE,				--Primary index is the data in a B- tree format.
--  iUnitKey				int				NOT NULL FOREIGN KEY REFERENCES  tUnit(iUnitKey),
--  iTypeKey				int				NOT NULL FOREIGN KEY REFERENCES  tType(iTypeKey),
--  PRIMARY KEY (iTYpeKey, iUnitKey)
--}
--GO

CREATE TABLE tReading(		--	drop table treading
  iReadingsKey			int				NOT NULL PRIMARY KEY CLUSTERED identity(4,10),				--Primary index is the data in a B- tree format.
  iTypeNumber			int				NOT NULL FOREIGN KEY REFERENCES tType(iTypeNumber),
  iUnitNumber			int				NOT NULL FOREIGN KEY REFERENCES tUnit(iUnitNumber),
  datDateTime			smalldatetime	NOT NULL,
  dValue				float(53)		NOT NULL
)
GO




------------------------------
USE DogsData
GO

INSERT INTO tDepartment (acName, iDepartmentNumber) VALUES ('123 Rabbit Lane', 1)
SELECT * FROM tDepartment

--What type of sensor
INSERT INTO tType (acName, iTypeNumber) VALUES ('Temperature', 10)
INSERT INTO tType (acName, iTypeNumber) VALUES ('Moisture', 20)
INSERT INTO tType (acName, iTypeNumber) VALUES ('Moisture 2', 30)
SELECT * FROM tType

INSERT INTO tUnit (iDepartmentKey, acName, iUnitNumber) VALUES (1, 'Front Lawn', 15)
INSERT INTO tUnit (iDepartmentKey, acName, iUnitNumber) VALUES (1, 'Back Lawn', 25)
SELECT * from tUNIT

-- THE LISTENER's FORMS OF ENTRY TO AN EXISTING SYSTEM

INSERT INTO tReading (iTypeNumber, iUnitNumber, datDateTime, dValue) VALUES (20, 15, '04/22/2015 3:55 am', 115)
INSERT INTO tReading (iTypeNumber, iUnitNumber, datDateTime, dValue) VALUES (20, 15, '04/22/2015 4:00 am', 110)
INSERT INTO tReading (iTypeNumber, iUnitNumber, datDateTime, dValue) VALUES (20, 15, '04/22/2015 4:15 am', 111)
INSERT INTO tReading (iTypeNumber, iUnitNumber, datDateTime, dValue) VALUES (20, 15, '04/22/2015 5:00 am', 99)
INSERT INTO tReading (iTypeNumber, iUnitNumber, datDateTime, dValue) VALUES (20, 15, '04/22/2015 1:00 pm', 66)
INSERT INTO tReading (iTypeNumber, iUnitNumber, datDateTime, dValue) VALUES (20, 15, '04/22/2015 3:00 pm', 220)
INSERT INTO tReading (iTypeNumber, iUnitNumber, datDateTime, dValue) VALUES (20, 15, 'April 22, 2015 03:00', 220)
INSERT INTO tReading (iTypeNumber, iUnitNumber, datDateTime, dValue) VALUES (20, 15, '2015-04-22 18:00', 221)
INSERT INTO tReading (iTypeNumber, iUnitNumber, datDateTime, dValue) VALUES (20, 15, '22APR2015 18:23', 211)

--The SQL statement the web page will give to the graphing unit (subject to approval).
SELECT datDateTime, dValue FROM tReading Where iTypeNumber = 20 AND iUnitNumber = 15 AND datDateTime > '04/22/2015 3:00 am' AND datDateTime < '04/23/2015 3:30 am' ORDER BY datDateTime

