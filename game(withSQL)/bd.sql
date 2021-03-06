USE [master]
GO
/****** Object:  Database [gameDB]    Script Date: 12.01.2021 13:17:26 ******/
CREATE DATABASE [gameDB]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'gameDB', FILENAME = N'D:\SQL\MSSQL15.MSSQLSERVER\MSSQL\DATA\gameDB.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'gameDB_log', FILENAME = N'D:\SQL\MSSQL15.MSSQLSERVER\MSSQL\DATA\gameDB_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [gameDB] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [gameDB].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [gameDB] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [gameDB] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [gameDB] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [gameDB] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [gameDB] SET ARITHABORT OFF 
GO
ALTER DATABASE [gameDB] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [gameDB] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [gameDB] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [gameDB] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [gameDB] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [gameDB] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [gameDB] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [gameDB] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [gameDB] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [gameDB] SET  DISABLE_BROKER 
GO
ALTER DATABASE [gameDB] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [gameDB] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [gameDB] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [gameDB] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [gameDB] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [gameDB] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [gameDB] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [gameDB] SET RECOVERY FULL 
GO
ALTER DATABASE [gameDB] SET  MULTI_USER 
GO
ALTER DATABASE [gameDB] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [gameDB] SET DB_CHAINING OFF 
GO
ALTER DATABASE [gameDB] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [gameDB] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [gameDB] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [gameDB] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'gameDB', N'ON'
GO
ALTER DATABASE [gameDB] SET QUERY_STORE = OFF
GO
USE [gameDB]
GO
/****** Object:  Table [dbo].[audio]    Script Date: 12.01.2021 13:17:26 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[audio](
	[id_audio] [int] IDENTITY(1,1) NOT NULL,
	[id_game_level] [int] NULL,
	[author] [varchar](1) NULL,
	[name] [varchar](1) NULL,
PRIMARY KEY CLUSTERED 
(
	[id_audio] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[card]    Script Date: 12.01.2021 13:17:26 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[card](
	[id_card] [int] IDENTITY(1,1) NOT NULL,
	[id_talent] [int] NULL,
	[id_image] [int] NULL,
	[point] [varchar](max) NULL,
	[type] [varchar](max) NULL,
	[usability] [varchar](max) NULL,
 CONSTRAINT [PK__card__C71FE367292A5E3F] PRIMARY KEY CLUSTERED 
(
	[id_card] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[effect]    Script Date: 12.01.2021 13:17:26 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[effect](
	[id_effect] [int] IDENTITY(1,1) NOT NULL,
	[name] [varchar](max) NULL,
	[activity] [varchar](max) NULL,
	[strength] [int] NULL,
	[step_count] [int] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[enemy]    Script Date: 12.01.2021 13:17:26 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[enemy](
	[id_enemy] [int] IDENTITY(1,1) NOT NULL,
	[id_game_level] [int] NULL,
	[name] [varchar](max) NULL,
	[normal_damage] [int] NULL,
	[experience] [float] NULL,
	[max_health_point] [int] NULL,
	[health_point] [int] NULL,
	[type] [varchar](max) NULL,
	[activity] [varchar](max) NULL,
 CONSTRAINT [PK__enemy__D08FD2E3BDAD6589] PRIMARY KEY CLUSTERED 
(
	[id_enemy] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[enemy_emergence]    Script Date: 12.01.2021 13:17:26 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[enemy_emergence](
	[id_enemy_emergence] [int] IDENTITY(1,1) NOT NULL,
	[id_enemy] [int] NULL,
	[emergence_count] [int] NULL,
	[passed] [varchar](max) NULL,
 CONSTRAINT [PK__enemy_sk__CC8106DC45302830] PRIMARY KEY CLUSTERED 
(
	[id_enemy_emergence] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[game_level]    Script Date: 12.01.2021 13:17:26 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[game_level](
	[id_game_level] [int] IDENTITY(1,1) NOT NULL,
	[max_step_count] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[id_game_level] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[image]    Script Date: 12.01.2021 13:17:26 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[image](
	[id_image] [int] IDENTITY(1,1) NOT NULL,
	[id_game_level] [int] NULL,
	[name] [varchar](max) NULL,
	[path] [varchar](max) NULL,
	[purpose] [varchar](max) NULL,
	[width] [int] NULL,
	[height] [int] NULL,
	[posX] [int] NULL,
	[posY] [int] NULL,
 CONSTRAINT [PK__image__C28C621CF0728F78] PRIMARY KEY CLUSTERED 
(
	[id_image] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[player]    Script Date: 12.01.2021 13:17:26 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[player](
	[id_player] [int] IDENTITY(1,1) NOT NULL,
	[id_game_level] [int] NULL,
	[ip] [varchar](max) NULL,
	[username] [varchar](max) NULL,
	[strength] [varchar](max) NULL,
 CONSTRAINT [PK__player__45CF72B16BA167BB] PRIMARY KEY CLUSTERED 
(
	[id_player] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[player_state]    Script Date: 12.01.2021 13:17:26 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[player_state](
	[id_player_state] [int] IDENTITY(1,1) NOT NULL,
	[id_player] [int] NULL,
	[health_point] [int] NULL,
	[experience] [float] NULL,
	[max_experience] [float] NULL,
 CONSTRAINT [PK__player_s__CA6A057565C60964] PRIMARY KEY CLUSTERED 
(
	[id_player_state] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[talent]    Script Date: 12.01.2021 13:17:26 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[talent](
	[id_talent] [int] IDENTITY(1,1) NOT NULL,
	[name] [varchar](max) NULL,
	[description] [varchar](max) NULL,
	[required_level] [int] NULL,
	[activity] [varchar](max) NULL,
	[posX] [int] NULL,
	[posY] [int] NULL,
 CONSTRAINT [PK__talent__035ED3E04890F337] PRIMARY KEY CLUSTERED 
(
	[id_talent] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
SET IDENTITY_INSERT [dbo].[card] ON 

INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (1, 1, 1, N'5', N'atk', N'used')
INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (2, 1, 2, N'10', N'atk', N'used')
INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (3, 1, 3, N'15', N'atk', N'used')
INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (4, 1, 4, N'20', N'atk', N'used')
INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (5, 2, 5, N'5', N'blood', N'not used')
INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (6, 2, 6, N'10', N'blood', N'not used')
INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (7, 2, 7, N'15', N'blood', N'not used')
INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (8, 2, 8, N'20', N'blood', N'not used')
INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (9, 3, 9, N'5', N'fire', N'not used')
INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (10, 3, 10, N'10', N'fire', N'not used')
INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (11, 3, 11, N'15', N'fire', N'not used')
INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (12, 3, 12, N'20', N'fire', N'not used')
INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (13, 4, 13, N'5', N'shield', N'not used')
INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (14, 4, 14, N'10', N'shield', N'not used')
INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (15, 4, 15, N'15', N'shield', N'not used')
INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (16, 4, 16, N'20', N'shield', N'not used')
INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (17, 6, 18, N'5', N'heal', N'not used')
INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (18, 6, 19, N'10', N'heal', N'not used')
INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (19, 6, 20, N'15', N'heal', N'not used')
INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (20, 6, 21, N'20', N'heal', N'not used')
INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (21, 7, 43, N'5', N'vamp', N'not used')
INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (22, 7, 44, N'10', N'vamp', N'not used')
INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (23, 7, 45, N'15', N'vamp', N'not used')
INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (24, 7, 46, N'20', N'vamp', N'not used')
INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (25, 8, 1049, N'5', N'repulse', N'not used')
INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (26, 8, 1050, N'10', N'repulse', N'not used')
INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (27, 8, 1051, N'15', N'repulse', N'not used')
INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (28, 8, 1052, N'20', N'repulse', N'not used')
INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (29, 9, 1053, N'5', N'freeze', N'not used')
INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (30, 9, 1054, N'10', N'freeze', N'not used')
INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (31, 9, 1055, N'15', N'freeze', N'not used')
INSERT [dbo].[card] ([id_card], [id_talent], [id_image], [point], [type], [usability]) VALUES (32, 9, 1056, N'20', N'freeze', N'not used')
SET IDENTITY_INSERT [dbo].[card] OFF
GO
SET IDENTITY_INSERT [dbo].[effect] ON 

INSERT [dbo].[effect] ([id_effect], [name], [activity], [strength], [step_count]) VALUES (1, N'Bleeding', N'false', 0, 0)
INSERT [dbo].[effect] ([id_effect], [name], [activity], [strength], [step_count]) VALUES (2, N'Burning', N'false', 0, 0)
INSERT [dbo].[effect] ([id_effect], [name], [activity], [strength], [step_count]) VALUES (3, N'Shield', N'false', 0, 0)
INSERT [dbo].[effect] ([id_effect], [name], [activity], [strength], [step_count]) VALUES (4, N'CleverTrick', N'false', 0, 0)
INSERT [dbo].[effect] ([id_effect], [name], [activity], [strength], [step_count]) VALUES (5, N'Vampirism', N'false', 0, 0)
INSERT [dbo].[effect] ([id_effect], [name], [activity], [strength], [step_count]) VALUES (6, N'Repulse', N'false', 0, 0)
INSERT [dbo].[effect] ([id_effect], [name], [activity], [strength], [step_count]) VALUES (7, N'Freezing', N'false', 0, 0)
INSERT [dbo].[effect] ([id_effect], [name], [activity], [strength], [step_count]) VALUES (8, N'Bite', N'false', 0, 0)
INSERT [dbo].[effect] ([id_effect], [name], [activity], [strength], [step_count]) VALUES (9, N'Bottle', N'false', 0, 0)
INSERT [dbo].[effect] ([id_effect], [name], [activity], [strength], [step_count]) VALUES (10, N'Dark', N'false', 0, 0)
INSERT [dbo].[effect] ([id_effect], [name], [activity], [strength], [step_count]) VALUES (11, N'Fly', N'false', 0, 0)
SET IDENTITY_INSERT [dbo].[effect] OFF
GO
SET IDENTITY_INSERT [dbo].[enemy] ON 

INSERT [dbo].[enemy] ([id_enemy], [id_game_level], [name], [normal_damage], [experience], [max_health_point], [health_point], [type], [activity]) VALUES (1, 1, N'Slime', 5, 3, 30, 30, N'usual', N'false')
INSERT [dbo].[enemy] ([id_enemy], [id_game_level], [name], [normal_damage], [experience], [max_health_point], [health_point], [type], [activity]) VALUES (2, 1, N'Dog', 5, 5, 50, 50, N'usual', N'false')
INSERT [dbo].[enemy] ([id_enemy], [id_game_level], [name], [normal_damage], [experience], [max_health_point], [health_point], [type], [activity]) VALUES (3, 1, N'Alice', 10, NULL, 200, 200, N'boss', N'false')
INSERT [dbo].[enemy] ([id_enemy], [id_game_level], [name], [normal_damage], [experience], [max_health_point], [health_point], [type], [activity]) VALUES (4, 1, N'Chest', 0, 0, 1, 1, N'chest', N'false')
INSERT [dbo].[enemy] ([id_enemy], [id_game_level], [name], [normal_damage], [experience], [max_health_point], [health_point], [type], [activity]) VALUES (5, 2, N'Bullfinch', 5, 3, 30, 30, N'usual', N'false')
INSERT [dbo].[enemy] ([id_enemy], [id_game_level], [name], [normal_damage], [experience], [max_health_point], [health_point], [type], [activity]) VALUES (6, 2, N'Hen', 5, 3, 50, 50, N'usual', N'false')
INSERT [dbo].[enemy] ([id_enemy], [id_game_level], [name], [normal_damage], [experience], [max_health_point], [health_point], [type], [activity]) VALUES (7, 2, N'Owl', 10, 5, 40, 40, N'usual', N'false')
INSERT [dbo].[enemy] ([id_enemy], [id_game_level], [name], [normal_damage], [experience], [max_health_point], [health_point], [type], [activity]) VALUES (8, 2, N'Magpie', 5, NULL, 200, 200, N'boss', N'false')
INSERT [dbo].[enemy] ([id_enemy], [id_game_level], [name], [normal_damage], [experience], [max_health_point], [health_point], [type], [activity]) VALUES (9, 2, N'Chest', 0, 0, 1, 1, N'chest', N'false')
SET IDENTITY_INSERT [dbo].[enemy] OFF
GO
SET IDENTITY_INSERT [dbo].[enemy_emergence] ON 

INSERT [dbo].[enemy_emergence] ([id_enemy_emergence], [id_enemy], [emergence_count], [passed]) VALUES (1, 1, 25, N'false')
INSERT [dbo].[enemy_emergence] ([id_enemy_emergence], [id_enemy], [emergence_count], [passed]) VALUES (2, 1, 40, N'false')
INSERT [dbo].[enemy_emergence] ([id_enemy_emergence], [id_enemy], [emergence_count], [passed]) VALUES (3, 1, 70, N'false')
INSERT [dbo].[enemy_emergence] ([id_enemy_emergence], [id_enemy], [emergence_count], [passed]) VALUES (4, 1, 75, N'false')
INSERT [dbo].[enemy_emergence] ([id_enemy_emergence], [id_enemy], [emergence_count], [passed]) VALUES (5, 2, 95, N'false')
INSERT [dbo].[enemy_emergence] ([id_enemy_emergence], [id_enemy], [emergence_count], [passed]) VALUES (6, 2, 125, N'false')
INSERT [dbo].[enemy_emergence] ([id_enemy_emergence], [id_enemy], [emergence_count], [passed]) VALUES (7, 2, 155, N'false')
INSERT [dbo].[enemy_emergence] ([id_enemy_emergence], [id_enemy], [emergence_count], [passed]) VALUES (8, 2, 160, N'false')
INSERT [dbo].[enemy_emergence] ([id_enemy_emergence], [id_enemy], [emergence_count], [passed]) VALUES (9, 3, 200, N'false')
INSERT [dbo].[enemy_emergence] ([id_enemy_emergence], [id_enemy], [emergence_count], [passed]) VALUES (10, 4, 85, N'false')
INSERT [dbo].[enemy_emergence] ([id_enemy_emergence], [id_enemy], [emergence_count], [passed]) VALUES (11, 5, 25, N'false')
INSERT [dbo].[enemy_emergence] ([id_enemy_emergence], [id_enemy], [emergence_count], [passed]) VALUES (12, 5, 30, N'false')
INSERT [dbo].[enemy_emergence] ([id_enemy_emergence], [id_enemy], [emergence_count], [passed]) VALUES (13, 5, 70, N'false')
INSERT [dbo].[enemy_emergence] ([id_enemy_emergence], [id_enemy], [emergence_count], [passed]) VALUES (14, 5, 85, N'false')
INSERT [dbo].[enemy_emergence] ([id_enemy_emergence], [id_enemy], [emergence_count], [passed]) VALUES (15, 5, 100, N'false')
INSERT [dbo].[enemy_emergence] ([id_enemy_emergence], [id_enemy], [emergence_count], [passed]) VALUES (16, 5, 130, N'false')
INSERT [dbo].[enemy_emergence] ([id_enemy_emergence], [id_enemy], [emergence_count], [passed]) VALUES (17, 6, 135, N'false')
INSERT [dbo].[enemy_emergence] ([id_enemy_emergence], [id_enemy], [emergence_count], [passed]) VALUES (18, 6, 150, N'false')
INSERT [dbo].[enemy_emergence] ([id_enemy_emergence], [id_enemy], [emergence_count], [passed]) VALUES (19, 6, 190, N'false')
INSERT [dbo].[enemy_emergence] ([id_enemy_emergence], [id_enemy], [emergence_count], [passed]) VALUES (20, 6, 210, N'false')
INSERT [dbo].[enemy_emergence] ([id_enemy_emergence], [id_enemy], [emergence_count], [passed]) VALUES (21, 6, 235, N'false')
INSERT [dbo].[enemy_emergence] ([id_enemy_emergence], [id_enemy], [emergence_count], [passed]) VALUES (22, 7, 270, N'false')
INSERT [dbo].[enemy_emergence] ([id_enemy_emergence], [id_enemy], [emergence_count], [passed]) VALUES (23, 7, 280, N'false')
INSERT [dbo].[enemy_emergence] ([id_enemy_emergence], [id_enemy], [emergence_count], [passed]) VALUES (24, 7, 300, N'false')
INSERT [dbo].[enemy_emergence] ([id_enemy_emergence], [id_enemy], [emergence_count], [passed]) VALUES (25, 7, 340, N'false')
INSERT [dbo].[enemy_emergence] ([id_enemy_emergence], [id_enemy], [emergence_count], [passed]) VALUES (26, 7, 350, N'false')
INSERT [dbo].[enemy_emergence] ([id_enemy_emergence], [id_enemy], [emergence_count], [passed]) VALUES (27, 8, 365, N'false')
INSERT [dbo].[enemy_emergence] ([id_enemy_emergence], [id_enemy], [emergence_count], [passed]) VALUES (28, 9, 200, N'false')
SET IDENTITY_INSERT [dbo].[enemy_emergence] OFF
GO
SET IDENTITY_INSERT [dbo].[game_level] ON 

INSERT [dbo].[game_level] ([id_game_level], [max_step_count]) VALUES (1, 200)
INSERT [dbo].[game_level] ([id_game_level], [max_step_count]) VALUES (2, 365)
SET IDENTITY_INSERT [dbo].[game_level] OFF
GO
SET IDENTITY_INSERT [dbo].[image] ON 

INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1, NULL, N'Card Atk 5', N'image/card/5(1).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (2, NULL, N'Card Atk 10', N'image/card/10(1).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (3, NULL, N'Card Atk 15', N'image/card/15(1).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (4, NULL, N'Card Atk 20', N'image/card/20(1).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (5, NULL, N'Card Blood 5', N'image/card/5(2).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (6, NULL, N'Card Blood 10', N'image/card/10(2).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (7, NULL, N'Card Blood 15', N'image/card/15(2).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (8, NULL, N'Card Blood 20', N'image/card/20(2).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (9, NULL, N'Card Fire 5', N'image/card/5(3).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (10, NULL, N'Card Fire 10', N'image/card/10(3).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (11, NULL, N'Card Fire 15', N'image/card/15(3).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (12, NULL, N'Card Fire 20', N'image/card/20(3).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (13, NULL, N'Card Shield 5', N'image/card/5(4).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (14, NULL, N'Card Shield 10', N'image/card/10(4).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (15, NULL, N'Card Shield 15', N'image/card/15(4).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (16, NULL, N'Card Shield 20', N'image/card/20(4).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (17, NULL, N'Card Clever Trick', N'image/card/5(5).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (18, NULL, N'Card Heal 5', N'image/card/5(6).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (19, NULL, N'Card Heal 10', N'image/card/10(6).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (20, NULL, N'Card Heal 15', N'image/card/15(6).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (21, NULL, N'Card Heal 20', N'image/card/20(6).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (22, NULL, N'No card', N'image/card/noCard.png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (23, 1, N'Background 1 lvl', N'image/background/1.png', N'background', 1000, 600, 0, 0)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (24, NULL, N'Hero window', N'image/details/hero.png', N'detail', 190, 300, 40, 280)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (25, 1, N'Step line 1', N'image/details/line1.png', N'detail', 600, 30, 200, 30)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (26, NULL, N'Mob window', N'image/details/mob.png', N'detail', 190, 300, 770, 280)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (27, NULL, N'Talent tree button', N'image/details/state.png', N'detail', 140, 50, 30, 20)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (28, NULL, N'Blood effect', N'image/effect/mobblood.png', N'effect', 190, 300, 770, 280)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (29, NULL, N'Fire effect', N'image/effect/mobfire.png', N'effect', 190, 300, 770, 280)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (30, 1, N'Alice', N'image/mob/Alice.png', N'mob', 190, 300, 770, 280)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (31, 1, N'Alice', N'image/mob/Alice1.png', N'mob', 380, 700, 400, 60)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (32, 1, N'Alice(angry)', N'image/mob/Alice2.png', N'mob', 380, 700, 400, 40)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (33, 1, N'Slime', N'image/mob/slime.png', N'mob', 190, 300, 770, 280)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (34, NULL, N'Talent choice', N'image/talent/choice.png', N'talent', 400, 500, 300, 50)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (35, NULL, N'Talent tree', N'image/talent/tree.png', N'talent', 400, 500, 300, 50)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (36, NULL, N'Talent active cell', N'image/talent/treeActive.png', N'talent', 90, 85, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (37, NULL, N'Chest', N'image/mob/chest(1).png', N'mob', 250, 200, 370, 220)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (38, NULL, N'Chest(open)', N'image/mob/chest(2).png', N'mob', 450, 350, 270, 85)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (39, 1, N'Dog', N'image/mob/dog(1).png', N'mob', 190, 300, 770, 280)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (40, 1, N'Dog', N'image/mob/dog(2).png', N'mob', 400, 330, 300, 100)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (41, NULL, N'Bite effect', N'image/effect/playerbite.png', N'effect', 190, 300, 40, 280)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (42, 1, N'Alice(laughs)', N'image/mob/Alice3.png', N'mob', 300, 700, 400, 60)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (43, NULL, N'Card Vamp 5', N'image/card/5(7).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (44, NULL, N'Card Vamp 10', N'image/card/10(7).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (45, NULL, N'Card Vamp 15', N'image/card/15(7).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (46, NULL, N'Card Vamp 20', N'image/card/20(7).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (47, NULL, N'NewGame', N'image/menu/new.png', N'menu', 1000, 600, 0, 0)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (48, NULL, N'LoadGame', N'image/menu/load.png', N'menu', 1000, 600, 0, 0)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (49, NULL, N'NoChoice', N'image/menu/no.png', N'menu', 1000, 600, 0, 0)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (50, NULL, N'Help', N'image/menu/help.png', N'menu', 1000, 600, 0, 0)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (51, NULL, N'Exit', N'image/menu/exit.png', N'menu', 1000, 600, 0, 0)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (52, NULL, N'EnterName', N'image/menu/name.png', N'menu', 1000, 600, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1047, NULL, N'MenuButton', N'image/details/menu.png', N'detail', 140, 50, 830, 20)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1048, NULL, N'transitionToMenu', N'image/transition/toMenu.png', N'transition', 1000, 600, 0, 0)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1049, NULL, N'Card Repulce 5', N'image/card/5(8).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1050, NULL, N'Card Repulce 10', N'image/card/10(8).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1051, NULL, N'Card Repulce 15', N'image/card/15(8).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1052, NULL, N'Card Repulce 20', N'image/card/20(8).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1053, NULL, N'Card Freeze 5', N'image/card/5(9).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1054, NULL, N'Card Freeze 10', N'image/card/10(9).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1055, NULL, N'Card Freeze 15', N'image/card/15(9).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1056, NULL, N'Card Freeze 20', N'image/card/20(9).png', N'card', 100, 150, NULL, NULL)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1057, NULL, N'Win', N'image/transition/win.png', N'transition', 1000, 600, 0, 0)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1058, NULL, N'Lose', N'image/transition/lose.png', N'transition', 1000, 600, 0, 0)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1059, NULL, N'Vamp effect', N'image/effect/playervamp.png', N'effect', 190, 300, 40, 280)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1060, NULL, N'Repulse effect', N'image/effect/playerrepulse.png', N'effect', 190, 300, 40, 280)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1061, NULL, N'Shield effect', N'image/effect/playershield.png', N'effect', 190, 300, 40, 280)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1062, NULL, N'Freeze effect', N'image/effect/mobfreeze.png', N'effect', 190, 300, 770, 280)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1063, NULL, N'Bottle 0', N'image/effect/bottle0.png', N'bottle', 100, 128, 250, 280)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1064, NULL, N'Bottle 1', N'image/effect/bottle1.png', N'bottle', 100, 128, 250, 280)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1065, NULL, N'Bottle 2', N'image/effect/bottle2.png', N'bottle', 100, 128, 250, 280)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1066, NULL, N'Bottle 3', N'image/effect/bottle3.png', N'bottle', 100, 128, 250, 280)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1067, NULL, N'Bottle 4', N'image/effect/bottle4.png', N'bottle', 100, 128, 250, 280)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1068, NULL, N'Bottle 5', N'image/effect/bottle5.png', N'bottle', 100, 128, 250, 280)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1071, 2, N'Background 2 lvl', N'image/background/2.png', N'background', 1000, 600, 0, 0)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1072, 2, N'Step line 2', N'image/details/line2.png', N'detail', 600, 30, 200, 30)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1073, 2, N'Bullfinch', N'image/mob/bullfinch(1).png', N'mob', 290, 215, 350, 150)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1074, 2, N'Bullfinch', N'image/mob/bullfinch(2).png', N'mob', 190, 300, 770, 280)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1075, 2, N'Hen', N'image/mob/hen(1).png', N'mob', 430, 280, 300, 100)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1076, 2, N'Hen', N'image/mob/hen(2).png', N'mob', 190, 300, 770, 280)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1077, 2, N'Owl', N'image/mob/Owl(1).png', N'mob', 230, 350, 400, 70)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1078, 2, N'Owl', N'image/mob/Owl(3).png', N'mob', 190, 300, 770, 280)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1079, 2, N'Owl(dark)', N'image/mob/Owl(2).png', N'mob', 230, 350, 400, 70)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1080, 2, N'Dark', N'image/effect/dark.png', N'effect', 1000, 600, 0, 0)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1081, 2, N'Magpie', N'image/mob/magpie(1).png', N'mob', 800, 700, 0, 70)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1082, 2, N'Magpie', N'image/mob/magpie(3).png', N'mob', 190, 300, 770, 280)
INSERT [dbo].[image] ([id_image], [id_game_level], [name], [path], [purpose], [width], [height], [posX], [posY]) VALUES (1083, 2, N'Magpie(fly)', N'image/mob/magpie(2).png', N'mob', 1000, 600, 0, 0)
SET IDENTITY_INSERT [dbo].[image] OFF
GO
SET IDENTITY_INSERT [dbo].[player] ON 

INSERT [dbo].[player] ([id_player], [id_game_level], [ip], [username], [strength]) VALUES (1, 2, N'26.163.84.35', N'Kiseleva', N'norm')
INSERT [dbo].[player] ([id_player], [id_game_level], [ip], [username], [strength]) VALUES (4, 1, N'192.168.0.103', N'player', N'norm')
SET IDENTITY_INSERT [dbo].[player] OFF
GO
SET IDENTITY_INSERT [dbo].[player_state] ON 

INSERT [dbo].[player_state] ([id_player_state], [id_player], [health_point], [experience], [max_experience]) VALUES (1, 1, 150, 0, 0)
INSERT [dbo].[player_state] ([id_player_state], [id_player], [health_point], [experience], [max_experience]) VALUES (2, 4, 200, 0, 0)
SET IDENTITY_INSERT [dbo].[player_state] OFF
GO
SET IDENTITY_INSERT [dbo].[talent] ON 

INSERT [dbo].[talent] ([id_talent], [name], [description], [required_level], [activity], [posX], [posY]) VALUES (1, N'Обычный удар', N'Обычный удар наносящий столько урона, сколько указано на карте', 1, N'active', 450, 205)
INSERT [dbo].[talent] ([id_talent], [name], [description], [required_level], [activity], [posX], [posY]) VALUES (2, N'Кровотечение', N'Обычный удар с дополнительным эффектом кровотечения: эффект отнимает у противника по 2/3/4/5 единиц здоровья в течение 5 ходов(в зависимости от цифры на карточке). Эффект не стакается', 2, N'inactive', 380, 270)
INSERT [dbo].[talent] ([id_talent], [name], [description], [required_level], [activity], [posX], [posY]) VALUES (3, N'Поджог', N'Обычный удар с дополнительным эффектом поджога: эффект отнимает у противника по 2/3/4/5 единиц здоровья в течение 5 ходов(в зависимости от цифры на карточке). Эффект не стакается', 2, N'inactive', 524, 273)
INSERT [dbo].[talent] ([id_talent], [name], [description], [required_level], [activity], [posX], [posY]) VALUES (4, N'Блок', N'Накладывает на героя щит на 1 ход, блокирующий 50/60/70/80% урона', 3, N'inactive', 335, 353)
INSERT [dbo].[talent] ([id_talent], [name], [description], [required_level], [activity], [posX], [posY]) VALUES (5, N'Ловкий трюк', N'Позволяет после использования 3 карт обновить их, оставив одну на руках', 3, N'inactive', 450, 353)
INSERT [dbo].[talent] ([id_talent], [name], [description], [required_level], [activity], [posX], [posY]) VALUES (6, N'Исцеление', N'Мгновенно исцеляет 20/30/40/50 единиц здоровья герою', 3, N'inactive', 575, 354)
INSERT [dbo].[talent] ([id_talent], [name], [description], [required_level], [activity], [posX], [posY]) VALUES (7, N'Вампиризм', N'В течение 3 ходов, когда герой атакует, он восполняет свою жизнь на 40/50/60/70% от своего урона', 4, N'inactive', 333, 452)
INSERT [dbo].[talent] ([id_talent], [name], [description], [required_level], [activity], [posX], [posY]) VALUES (8, N'Отразить удар', N'Накладывает на героя щит на 1 ход, блокирующий 50/60/70/80% урона и наносящий противнику 50% заблокированного урона', 4, N'inactive', 450, 450)
INSERT [dbo].[talent] ([id_talent], [name], [description], [required_level], [activity], [posX], [posY]) VALUES (9, N'Заморозка', N'Ударяет противника и замораживает его на 1 ход, из-за чего он пропускает свой следующий ход', 4, N'inactive', 574, 453)
SET IDENTITY_INSERT [dbo].[talent] OFF
GO
/****** Object:  Index [PK_effect]    Script Date: 12.01.2021 13:17:26 ******/
ALTER TABLE [dbo].[effect] ADD  CONSTRAINT [PK_effect] PRIMARY KEY NONCLUSTERED 
(
	[id_effect] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
ALTER TABLE [dbo].[audio]  WITH CHECK ADD FOREIGN KEY([id_game_level])
REFERENCES [dbo].[game_level] ([id_game_level])
GO
ALTER TABLE [dbo].[card]  WITH CHECK ADD  CONSTRAINT [FK__card__id_image__37A5467C] FOREIGN KEY([id_image])
REFERENCES [dbo].[image] ([id_image])
GO
ALTER TABLE [dbo].[card] CHECK CONSTRAINT [FK__card__id_image__37A5467C]
GO
ALTER TABLE [dbo].[card]  WITH CHECK ADD  CONSTRAINT [FK__card__id_talent__36B12243] FOREIGN KEY([id_talent])
REFERENCES [dbo].[talent] ([id_talent])
GO
ALTER TABLE [dbo].[card] CHECK CONSTRAINT [FK__card__id_talent__36B12243]
GO
ALTER TABLE [dbo].[enemy]  WITH CHECK ADD  CONSTRAINT [FK__enemy__id_game_l__3A81B327] FOREIGN KEY([id_game_level])
REFERENCES [dbo].[game_level] ([id_game_level])
GO
ALTER TABLE [dbo].[enemy] CHECK CONSTRAINT [FK__enemy__id_game_l__3A81B327]
GO
ALTER TABLE [dbo].[enemy_emergence]  WITH CHECK ADD  CONSTRAINT [FK__enemy_ski__id_en__3C69FB99] FOREIGN KEY([id_enemy])
REFERENCES [dbo].[enemy] ([id_enemy])
GO
ALTER TABLE [dbo].[enemy_emergence] CHECK CONSTRAINT [FK__enemy_ski__id_en__3C69FB99]
GO
ALTER TABLE [dbo].[image]  WITH CHECK ADD  CONSTRAINT [FK__image__id_game_l__38996AB5] FOREIGN KEY([id_game_level])
REFERENCES [dbo].[game_level] ([id_game_level])
GO
ALTER TABLE [dbo].[image] CHECK CONSTRAINT [FK__image__id_game_l__38996AB5]
GO
ALTER TABLE [dbo].[player]  WITH CHECK ADD  CONSTRAINT [FK__player__id_game___3A81B327] FOREIGN KEY([id_game_level])
REFERENCES [dbo].[game_level] ([id_game_level])
GO
ALTER TABLE [dbo].[player] CHECK CONSTRAINT [FK__player__id_game___3A81B327]
GO
ALTER TABLE [dbo].[player_state]  WITH CHECK ADD  CONSTRAINT [FK__player_st__id_pl__3B75D760] FOREIGN KEY([id_player])
REFERENCES [dbo].[player] ([id_player])
GO
ALTER TABLE [dbo].[player_state] CHECK CONSTRAINT [FK__player_st__id_pl__3B75D760]
GO
USE [master]
GO
ALTER DATABASE [gameDB] SET  READ_WRITE 
GO
