create table Treningsokt(
	Id int not null auto_increment,
	Dato date,
	Tidspunkt integer,
	Varighet integer,
	Notat varchar(200),
	PersonligPrestasjon integer,
	PersonligForm integer,
	InneUte varchar(15),
	Luftkvalitet varchar(30),
	Tilskuere integer,
	Temperatur integer,
	Vaertype varchar(30),
	constraint Treningsokt_PK primary key (Id));
	
create table Ovelse(
	Id int not null,
	Navn varchar(60),
	Beskrivelse varchar(200),
	TypeOvelse varchar(15),
	Belastning integer,
	AntallRep integer,
	AntallSet integer,
	Avstand integer, 
	Varighet integer,
	constraint Ovelse_PK primary key (Id));
	
create table Format(
	Id int not null,
	TypeTrening varchar(15),
	AntallSet integer,
	AntallRep integer,
	Varighet integer,
	Avstand integer,
	constraint Format_PK primary key (Id));
	
create table Mal(
	Id int not null,
	DatoFra date,
	DatoTil date,
	OvelseId integer not null,
	constraint Mal_PK primary key (Id)
	constraint Mal_FK foreign key (OvelseId) references Ovelse(OvelseId)
		on delete cascade
		on update cascade);

create table Resultat(
	FormatId int not null,
	TreningsoktId int not null,
	OvelseId int not null,
	constraint Resultat_FK1 foreign key (FormatId) references Format (Id)
		on delete cascade
		on update cascade
	constraint Resultat_FK2 foreign key (TreningsoktId) references Treningsokt(TreningsoktId)
		on delete cascade
		on update cascade
	constraint Resultat_FK3 foreign key (OvelseId) references Ovelse(OvelseId)
		on delete set null
		on update cascade);
	
create table Gruppe(
	Id int not null,
	Navn varchar(30),
	Beskrivelse varchar(200));
	
create table Delovelse(
	OvelseId int,
	GruppeId int,
	constraint Delovelse_FK1 foreign key (OvelseId) references Ovelse(OvelseId)
		on delete set null
		on update cascade
	constraint Delovelse_FK2 foreign key (GruppeId) references Gruppe(GruppeId)
		on delete set null
		on update cascade);
	
create table Delgruppe(
	Gruppe1Id int,
	Gruppe2Id int,
	constraint Delgruppe_FK1 foreign key (GruppeID) references Gruppe(Gruppe1Id)
		on delete set null
		on update cascade
	constraint Delgruppe_FK2 foreign key (GruppeId) references Gruppe(Gruppe2Id)
		on delete set null
		on update cascade);