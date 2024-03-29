USE [master]
GO
/****** Object:  Database [Analytics]    Script Date: 06/28/2012 15:12:26 ******/
CREATE DATABASE [Analytics] ON  PRIMARY 
( NAME = N'Analytics', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL10_50.MSSQLSERVER\MSSQL\DATA\Analytics.mdf' , SIZE = 509952KB , MAXSIZE = UNLIMITED, FILEGROWTH = 1024KB )
 LOG ON 
( NAME = N'Analytics_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL10_50.MSSQLSERVER\MSSQL\DATA\Analytics_log.ldf' , SIZE = 39296KB , MAXSIZE = 2048GB , FILEGROWTH = 10%)
GO
ALTER DATABASE [Analytics] SET COMPATIBILITY_LEVEL = 100
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [Analytics].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [Analytics] SET ANSI_NULL_DEFAULT OFF
GO
ALTER DATABASE [Analytics] SET ANSI_NULLS OFF
GO
ALTER DATABASE [Analytics] SET ANSI_PADDING OFF
GO
ALTER DATABASE [Analytics] SET ANSI_WARNINGS OFF
GO
ALTER DATABASE [Analytics] SET ARITHABORT OFF
GO
ALTER DATABASE [Analytics] SET AUTO_CLOSE OFF
GO
ALTER DATABASE [Analytics] SET AUTO_CREATE_STATISTICS ON
GO
ALTER DATABASE [Analytics] SET AUTO_SHRINK OFF
GO
ALTER DATABASE [Analytics] SET AUTO_UPDATE_STATISTICS ON
GO
ALTER DATABASE [Analytics] SET CURSOR_CLOSE_ON_COMMIT OFF
GO
ALTER DATABASE [Analytics] SET CURSOR_DEFAULT  GLOBAL
GO
ALTER DATABASE [Analytics] SET CONCAT_NULL_YIELDS_NULL OFF
GO
ALTER DATABASE [Analytics] SET NUMERIC_ROUNDABORT OFF
GO
ALTER DATABASE [Analytics] SET QUOTED_IDENTIFIER OFF
GO
ALTER DATABASE [Analytics] SET RECURSIVE_TRIGGERS OFF
GO
ALTER DATABASE [Analytics] SET  DISABLE_BROKER
GO
ALTER DATABASE [Analytics] SET AUTO_UPDATE_STATISTICS_ASYNC OFF
GO
ALTER DATABASE [Analytics] SET DATE_CORRELATION_OPTIMIZATION OFF
GO
ALTER DATABASE [Analytics] SET TRUSTWORTHY OFF
GO
ALTER DATABASE [Analytics] SET ALLOW_SNAPSHOT_ISOLATION OFF
GO
ALTER DATABASE [Analytics] SET PARAMETERIZATION SIMPLE
GO
ALTER DATABASE [Analytics] SET READ_COMMITTED_SNAPSHOT OFF
GO
ALTER DATABASE [Analytics] SET HONOR_BROKER_PRIORITY OFF
GO
ALTER DATABASE [Analytics] SET  READ_WRITE
GO
ALTER DATABASE [Analytics] SET RECOVERY FULL
GO
ALTER DATABASE [Analytics] SET  MULTI_USER
GO
ALTER DATABASE [Analytics] SET PAGE_VERIFY CHECKSUM
GO
ALTER DATABASE [Analytics] SET DB_CHAINING OFF
GO
EXEC sys.sp_db_vardecimal_storage_format N'Analytics', N'ON'
GO
USE [Analytics]
GO
/****** Object:  Table [dbo].[Analytics_Visits_Site]    Script Date: 06/28/2012 15:12:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Analytics_Visits_Site](
	[Analytics_Date] [date] NOT NULL,
	[Site] [nvarchar](255) NOT NULL,
	[UniqueVisitors] [int] NOT NULL,
	[Visits] [int] NULL,
 CONSTRAINT [PK_Analytics_Visits_Site] PRIMARY KEY CLUSTERED 
(
	[Analytics_Date] ASC,
	[Site] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Analytics_Visitor]    Script Date: 06/28/2012 15:12:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Analytics_Visitor](
	[Analytics_ID] [int] IDENTITY(1,1) NOT NULL,
	[LandingPagePath] [nvarchar](255) NULL,
	[TransactionID] [nvarchar](255) NULL,
	[DaysSinceLastVisit] [nvarchar](255) NULL,
	[PageDepth] [int] NULL,
	[VisitCount] [int] NULL,
	[IsNewVisitor] [bit] NULL
) ON [PRIMARY]
GO
CREATE NONCLUSTERED INDEX [IX_Analytics_Visitor_TransactionID] ON [dbo].[Analytics_Visitor] 
(
	[TransactionID] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Analytics_Source_Visits_Site]    Script Date: 06/28/2012 15:12:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Analytics_Source_Visits_Site](
	[Analytics_Date] [date] NOT NULL,
	[Site] [nvarchar](15) NOT NULL,
	[Medium] [nvarchar](50) NOT NULL,
	[UniqueVisitors] [int] NOT NULL,
	[Visits] [int] NULL,
	[Transactions] [int] NULL,
 CONSTRAINT [PK_Analytics_Source_Visits_Site] PRIMARY KEY CLUSTERED 
(
	[Analytics_Date] ASC,
	[Site] ASC,
	[Medium] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Analytics_Source_Time]    Script Date: 06/28/2012 15:12:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Analytics_Source_Time](
	[Analytics_ID] [int] IDENTITY(1,1) NOT NULL,
	[Campaign] [nvarchar](255) NULL,
	[Keyword] [nvarchar](255) NULL,
	[Medium] [nvarchar](255) NULL,
	[Source] [nvarchar](255) NULL,
	[TransactionID] [nvarchar](255) NULL,
	[DaysToTransaction] [int] NULL,
	[VisitsToTransaction] [int] NULL,
	[TrafficType] [nvarchar](255) NULL
) ON [PRIMARY]
GO
CREATE NONCLUSTERED INDEX [IX_Analytics_Source_Time_TransactionID] ON [dbo].[Analytics_Source_Time] 
(
	[TransactionID] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Analytics_Site_Account]    Script Date: 06/28/2012 15:12:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[Analytics_Site_Account](
	[Site] [int] NOT NULL,
	[Analytics_AccountID] [varchar](50) NOT NULL,
	[THG_Site] [bit] NULL,
	[Site_Code] [varchar](50) NULL
) ON [PRIMARY]
GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[Analytics_Search]    Script Date: 06/28/2012 15:12:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Analytics_Search](
	[Analytics_ID] [int] IDENTITY(1,1) NOT NULL,
	[TransactionID] [nvarchar](255) NULL,
	[SiteSearchUsed] [nvarchar](255) NULL,
	[VisitLength] [int] NULL
) ON [PRIMARY]
GO
CREATE NONCLUSTERED INDEX [IX_Analytics_Search_TransactionID] ON [dbo].[Analytics_Search] 
(
	[TransactionID] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Analytics_PaidSearch_Page]    Script Date: 06/28/2012 15:12:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Analytics_PaidSearch_Page](
	[Analytics_Date] [date] NOT NULL,
	[Site] [nvarchar](15) NOT NULL,
	[Source] [nvarchar](50) NOT NULL,
	[Medium] [nvarchar](50) NOT NULL,
	[PagePath] [nvarchar](255) NOT NULL,
	[Visits] [int] NULL,
 CONSTRAINT [PK_Analytics_PaidSearch_Page] PRIMARY KEY CLUSTERED 
(
	[Analytics_Date] ASC,
	[Site] ASC,
	[Source] ASC,
	[Medium] ASC,
	[PagePath] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Analytics_Geo_System]    Script Date: 06/28/2012 15:12:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Analytics_Geo_System](
	[Analytics_ID] [int] IDENTITY(1,1) NOT NULL,
	[City] [nvarchar](255) NULL,
	[Country] [nvarchar](255) NULL,
	[Language] [nvarchar](255) NULL,
	[TransactionId] [nvarchar](255) NULL,
	[isMobile] [bit] NULL
) ON [PRIMARY]
GO
CREATE NONCLUSTERED INDEX [IX_Analytics_Geo_System_TransactionId] ON [dbo].[Analytics_Geo_System] 
(
	[TransactionId] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Analytics_Event]    Script Date: 06/28/2012 15:12:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Analytics_Event](
	[Analytics_Date] [date] NOT NULL,
	[Site] [nvarchar](15) NOT NULL,
	[Category] [nvarchar](50) NOT NULL,
	[Action] [nvarchar](50) NOT NULL,
	[Label] [nvarchar](255) NOT NULL,
	[totalEvents] [int] NOT NULL,
	[uniqueEvents] [int] NULL,
 CONSTRAINT [PK_Analytics_Event] PRIMARY KEY CLUSTERED 
(
	[Analytics_Date] ASC,
	[Site] ASC,
	[Category] ASC,
	[Action] ASC,
	[Label] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Analytics_Affiliate]    Script Date: 06/28/2012 15:12:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Analytics_Affiliate](
	[id] [nvarchar](50) NOT NULL,
	[name] [nvarchar](255) NOT NULL,
	[website] [nvarchar](255) NULL,
 CONSTRAINT [PK_Analytics_Affiliate] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Analytics_Adwords_Cost]    Script Date: 06/28/2012 15:12:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Analytics_Adwords_Cost](
	[Id] [bigint] IDENTITY(1,1) NOT NULL,
	[GA_Account] [nvarchar](50) NOT NULL,
	[Date] [datetime] NOT NULL,
	[GA_Medium] [nvarchar](50) NOT NULL,
	[GA_Source] [nvarchar](50) NOT NULL,
	[GA_Adwords_Campaign] [nvarchar](50) NOT NULL,
	[GA_Ad_Cost] [money] NOT NULL,
	[GA_Transactions] [int] NOT NULL,
	[GA_Revenue] [money] NOT NULL,
	[GA_Keywords] [nvarchar](255) NOT NULL,
	[GA_Clicks] [int] NOT NULL,
 CONSTRAINT [PK_Adwords_Cost] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
CREATE NONCLUSTERED INDEX [IX_Analytics_Adword_Cost_Account_Date] ON [dbo].[Analytics_Adwords_Cost] 
(
	[GA_Account] ASC,
	[Date] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
GO
