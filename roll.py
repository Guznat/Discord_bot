from discord.ext import commands
import random



class Roll:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def viking_name(self, message):

        female = ['Aldis', ' Alfdisa', ' Alofa', ' Arngud', ' Asgerd', ' Astrid', ' Asvor', ' Aud',

                  'Bergthora', ' Berthora', ' Biorgej', ' Blenda', ' Bodvilda', ' Borga', ' Brynhilda',

                  'Freydhis', ' Frigerda',

                  'Gjaflauga', ' Gerda', ' Grima', ' Grjota', ' Groa', ' Gudhirda', ' Gudgruna', ' Gudny',
                  'Gudfinna', ' Gudrid', ' Gudrun', ' Gunhilda', ' Gyda',

                  'Halla', ' Halldis', ' Hallberga', ' Hallgerda', ' Hallveiga', ' Hekia', ' Helg', ' Herdis',
                  'Hervor', ' Hilda', ' Hildigunn', ' Hrafnhilda', ' Hrefna', ' Hrodna',

                  'Inbjorga', ' Ingibiorga', ' Ingunn', ' Jofridd', ' Joreid', ' Jorunn',

                  'Kadlin',

                  'Nidbjor',

                  'Olof', ' Ormiga', ' Osk',

                  'Rafarta', ' Ragnheida', ' Rangveig', ' Reginleifa',

                  'Sigrida', ' Svanlaug',

                  'Tharlauga', ' Thora', ' Thorbjorga', ' Thordis', ' Thoreja', ' Thorgerda', ' Thorguna',
                  'Thorhalla', ' Thorhilda', ' Thorlauga', ' Thorkatla', ' Thoroda', ' Thorunn', 'Thorvor',
                  'Thurid', ' Thyria',

                  'Ud', ' Unn',

                  'Valborga', ' Valgerd',

                  'Yngvild']
        male = ['Adils', ' Aegir', ' Agnar', ' Agni', ' Aki', ' Alf', ' Alrek', ' An', ' Ansgar', ' Ansculv', ' Ansulv',
                ' Anund', ' Arnlaug', ' Arinbjorn', ' Ari', ' Armod', ' Arnjolf', ' Arnbjorn', ' Arnfinn', ' Arnvald',
                ' Arnvind', ' Asbjorn', ' Asbrand', ' Asgaut', ' Asgeir', ' Asgrim', ' Ask', ' Aslak', ' Asleik',
                ' Asmund',
                ' Asolf', ' Asvald', ' Atli', ' Audmund', ' Audolf', ' Audun', ' Aun',
                'Bard', ' Beinir', ' Bersi', ' Birger', ' Bjalbo', ' Bjam', ' Bjarni', ' Bjorn', ' BjornolfBodvar',
                ' Borg',
                ' Bork', ' Bolli', ' Bolvark', ' Bragi', ' Brand', ' Brase', ' Brodir', ' Brynjolf',

                'Dallak',

                'Egil', ' Eid', ' Eilif', ' Einar', ' Eldgrim', ' Ellid', ' Emund', ' Erlend', ' Erling', ' Erp',
                ' Eryk',
                ' Esbiorn', ' Eskil', ' Eydis', ' Eyjolf', ' Eystein', ' Eyvald', ' Eyvind', ' Finnbogi', ' Floki',
                ' Flosi',
                ' Fridhleif', ' Frodi ',

                'Gamli ', ' Gard', ' Gardhar', ' Garm', ' Gaut', ' Geir', ' Geirmund', ' Geirstein', ' Gerbjorn',
                ' Gest',
                ' Giermund', ' Gili', ' Gilsi', ' Gizur', ' Gjaflaug', ' Glum', ' Godfred', ' Godred', ' Gorm',
                ' Grani',
                ' Grettir', ' Grim', ' Grimisdal', ' Gro', ' Gudfast', ' Gudfrid', ' Gudhleif', ' Gudlaug', ' Gudmund',
                ' Gudred', ' Gunlaug', ' Gunnald', ' Gunnar', ' Gunnbjorn', ' Guthurm', ' Gylve',

                'Haf', ' Hafgrim', ' Haki', ' Hakon', ' Halbjorn', ' Halfdan', ' Hall', ' Hallbjorn', ' Halldor',
                ' Hallfred',
                ' Hallgrim', ' Hallkell', ' Hallstein', ' Hallvard', ' Hamund', ' Harald', ' Hardekanut', ' Harek',
                ' Harjolf',
                ' Harp', ' Hastein', ' Hauk', ' Havard', ' Hedin', ' Helgi', 'Hergils', ' Herigar', ' Herjolf',
                ' Hermund',
                ' Herstein', ' Hjalti', ' Hjorleif', ' Hjort', ' Hlen', ' Hlodver', ' Hogni', ' Hognieg', ' Holmstein',
                ' Hord',
                ' Horik', ' Hoskuld', ' Hrafn', ' Hrafnkel', ' Hrapp', ' Hrein', ' Hroald', ' Hrolf', ' Hrut',
                ' Hunbogi',
                ' Hvamm', ' Hveinn', ' Hvit',

                'Illugi', ' Ingjald', ' Ingolf', ' Ingstad', ' Ingvar', ' Iostan', ' Isleif', ' Ivar', ' Jon',
                ' Jorund',

                'Kalf', ' Karl', ' Kari', ' Karlsefni', ' Ketill', ' Ketillbjorn', ' Kjallak', ' Kjartan', ' Knut',
                ' Kodran',
                ' Kolbein', ' Koll', ' Kolskegg', ' Kormak', ' Kotlell', ' Kvedulf', ' Lambi', ' Leif', ' Ljot',
                ' Lodmunnd',
                ' Lyting',

                'Mar', ' Magnu', ' Melkolf', ' Merlund', ' Modolf', ' Mord', ' Niels', ' Njal', ' Njor', ' Obland',
                ' Odd',
                ' Oddi', ' Oddr', ' Offa', ' Olaf', ' Ogmund', ' Ondott', ' Onund', ' Orm', ' Orn', ' Ornolt', ' Ospak',
                ' Osvald', ' Osvif', ' Osvir', ' Otkell', ' Otrygg', ' Ottar', ' Ozur', ' Ragi', ' Rafn', ' Ranulf',
                ' Ragnald',
                ' Ragnar', ' Rolf', ' Rollo', ' Rognvald', ' Runlof', ' Ruryk',

                'Saemund', ' Sigfus', ' Sigmunt', ' Sigtrygg', ' Sigurd', ' Sigvat', ' Sjusta', ' Skammkell', ' Skapti',
                ' Skarf', ' Skarphedin', ' Skeggi', ' Skidi', ' Skiun', ' Skjold', ' Skokkolf', ' Snaebjorn',
                ' Snorrri',
                ' Sofi', ' Solmund Solv', ' Sorli', ' Spjallbude', ' Starkad', ' Storolf', ' Sturla', ' Styr',
                ' Styrbjorn',
                ' Starkad', ' Stein', ' Steingrim', ' Steinthor', ' Stigandi', ' Styr', ' Sumarlidi', ' Surt', ' Svan',
                ' Svart',
                ' Sveinung', ' Sven', ' Sverri', ' Svertig',

                'Teit', ' Therarinn', ' Thidrand', ' Thjodol', ' Thjostolf', ' Thoralf', ' Thorarin', ' Thorberg',
                ' Thorbjorn',
                ' Thorbrand', ' Thord', ' Thore', ' Thorer', ' Thorfinn', ' Thorgal', ' Thorgeir', ' Thorgest',
                ' Thorgils',
                ' Thorgrim', ' Thorhal', ' Thorhild', ' Thorkell', ' Thorlak', ' Thorleif', ' Thorleik', ' Thorlof',
                ' Thormod',
                ' Thorny', ' Thorolf', ' Thorrad', ' Thorir', ' Thorodd', ' Thorrod', ' Thorstan', ' Thorstein',
                ' Thorvald',
                ' Thorvi', ' Thorvor', ' Thrugot', ' Tjordek', ' Tjorvi', ' Tofi', ' Toke', ' Torf', ' Torfi', ' Tosti',
                ' Trandill', ' Tubbe', ' Tyrker',

                'Ulf', ' Ulfar', ' Ulfberht', ' Ulfheidik',

                'Vakr', ' Valbrand', ' Valdemar', ' Valgard', ' Valthjolf', ' Vandil', ' Vandrad', ' Vermund',
                ' Vestar',
                ' Vestein', ' Vifil', ' Vigdisk', ' Vingor',

                'Yngvar']

        if message == 'female':
            name = random.choice(female)
            await self.client.say("Imię dla wylosowanej bohaterki to ||"+name+"||!")
        elif message == 'male':
            name = random.choice(male)
            await self.client.say("Imię dla wylosowanego bohatera to ||" + name + "||!")
        else:
            await self.client.say("Spróbuj $viking_name male / $viking_name female")



def setup(client):
    client.add_cog(Roll(client))