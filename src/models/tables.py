from models.dice import Dice
class Tables():
    def getClass(self):
        classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
        dice = Dice(len(classes))
        return classes[dice.roll()-1]

    def getRace(self):
        races = ["Dwarf", "Elf", "Halfling", "Human", "Dragonborn", "Gnome", "Half-elf", "Half-orc", "Tiefling"]
        dice = Dice(len(races))
        return races[dice.roll()-1]

    def getSubrace(self, race):
        if(race == "Dwarf"):
            subrace = ["Hill", "Mountain"]
            dice = Dice(len(subrace))
            return subrace[dice.roll()-1]
        elif (race == "Elf"):
            subrace = ["High", "Wood", "Dark"]
            dice = Dice(len(subrace))
            return subrace[dice.roll()-1]
        elif (race == "Halfling"):
            subrace = ["Lightfoot", "Stout"]
            dice = Dice(len(subrace))
            return subrace[dice.roll()-1]
        elif (race == "Human"):
            subrace = ["Normal", "Variant"]
            dice = Dice(len(subrace))
            return subrace[dice.roll()-1]
        elif (race == "Dragonborn"):
            subrace = ["Black", "Blue", "Brass", "Bronze", "Copper", "Gold", "Green", "Red", "Silver", "White"]
            dice = Dice(len(subrace))
            return subrace[dice.roll()-1]
        elif (race == "Gnome"):
            subrace = ["Forest", "Rock"]
            dice = Dice(len(subrace))
            return subrace[dice.roll()-1]
        elif (race == "Half-elf"):
            return "Normal"
        elif (race == "Half-orc"):
            return "Normal"
        elif (race == "Tiefling"):
            return "Normal"
        
    def getAlignment(self):
        alignment = ["Lawful good", "Neutral good", "Chaotic good", "Lawful neutraI", "Neutral", "Chaotic neutral", "Lawful evil", "Neutral evil", "Chaotic evil"]
        dice = Dice(len(alignment))
        return alignment[dice.roll()-1]

    def getName(self, race, genre):
        fullName = ""
        names = []
        if(race == "Dwarf"):
            if(genre == "Male"):
                names = ["Adrik", "Alberich", "Baern", "Barendd", "Brottor", "Bruenor", "Oain", "Oarrak", "Oelg", "Eberk", "Einkil", "Fargrim", "Flint", "Gardain", "Harbek", "Kildrak", "Morgran", "Orsik", "Oskar", "Rangrim", "Rurik", "Taklinn", "Thoradin", "Thorin", "Tordek", "Traubon", "Travok", "Ulfgar", "Veit", "Vondal"]
            if(genre == "Female"):
                names = ["Amber", "Artin", "Audhild", "Bardryn","Oagnal", "Oiesa", "Eldeth", "Falkrunn", "Finellen", "Gunnloda","Gurdis", "Helja", "Hlin", "Kathra", "Kristryd", "lide", "Liftrasa","Mardred", "Riswynn", "Sannl", "Torbera", "Torgga", "Vistra"]
            clan = ["Balderk", "Battlehammer", "Brawnanvil","Oankil", "Fireforge", "Frostbeard", "Gorunn", "Holderhek","Ironfist", "Loderr", "Lutgehr", "Rumnaheim", "Strakeln","Torunn", "Ungart"]
            diceName = Dice(len(names))
            diceClan = Dice(len(clan))
            fullName = names[diceName.roll()-1] + " " + clan[diceClan.roll()-1]

        if(race == "Elf"):
            if(genre == "Male"):
                names = ["Adran", "Aelar", "Aramil", "Arannis", "Aust", "Beiro", "Berrian", "Carrie", "Enialis", "Erdan", "Erevan", "Galinndan", "Hadarai", "Heian", "Himo. Immeral", "Ivellios", "Laucian", "Mindartis", "Paelias", "Peren", "Quarion", "Riardon", "Rolen", "Soveliss", "Thamior", "Tharivol", "Theren", "Varis"]
            if(genre == "Female"):
                names = ["Adrie", "Althaea", "Anastrianna", "Andraste", "Antinua", "Bethrynna", "Birel", "Caelynn", "Orusilia", "Enna", "Felosial", "lelenia", "jelenneth", "Keyleth", "Leshanna", "Lia", "Meriele", "Mialee", "Naivara", "Quelenna", "Quillathe", "Sariel", "Shanairra", "Shava", "Silaqui", "Theirastra", "Thia", "Vadania", "Valanthe", "Xanaphia"]
            clan = ["Amakiir(Gemflower)","Amastacia (Starflower)","Galanodel(Moonwhisper)","Holimion (Oiamonddew)","IIphelkiir(Gemblossom)","Liadon (Silverfrond)","Meliamne(Oakenheel)","Nailo (Nightbreeze)","Siannodel(Moonbrook)","Xiloscient (Goldpetal)"]
            diceName = Dice(len(names))
            diceClan = Dice(len(clan))
            fullName = names[diceName.roll()-1] + " " + clan[diceClan.roll()-1]

        if(race == "Halfling"):
            if(genre == "Male"):
                names = ["Alton","Ander","Cade","Corrin","Eldon","Errich","Finnan","Garret","Lindal","Lyle","Merric","Milo","Osborn","Perrin","Reed","Roscoe","Wellby"]
            if(genre == "Female"):
                names = ["Andry","Bree","Callie","Cora","Euphemia","jillian","Kithri","Lavinia","Lidda","Merla","Nedda","Paela","Portia","Seraphina","Shaena","Trym","Vani","Verna"]
            clan = ["Brushgather","Goodbarrel","Greenbottle","High-hill","Hilltopple","Leagallow","Tealeaf","Thorngage","Tosscobble","Underbough"]
            diceName = Dice(len(names))
            diceClan = Dice(len(clan))
            fullName = names[diceName.roll()-1] + " " + clan[diceClan.roll()-1]

        if(race == "Human"):
            if(genre == "Male"):
                names = ["Anlow","Arando","Bram","Cale","Dalkon","Daylen","Dodd","Dungarth","Dyrk","Eandro","Falken","Feck","Fenton","Gryphero","Hagar","Jeras","Krynt","Lavant","Leyten","Madian","Malfier","Markus","Meklan","Namen","Navaren","Nerle","Nilus","Ningyan","Norris","Quentin","Semil","Sevenson","Steveren","Talfen","Tamond","Taran","Tavon","Tegan","Vanan","Vincent"]
            if(genre == "Female"):
                names = ["Azura","Brey","Hallan","Kasaki","Lorelei","Mirabel","Pharana","Remora","Rosalyn","Sachil","Saidi","Tanika","Tura","Tylsa","Vencia","Xandrilla"]
            clan = ["Arkalis","Armanci","Bilger","Blackstrand","Brightwater","Carnavon","Caskajaro","Coldshore","Coyle","Cresthill","Cuttlescar","Daargen","Dalicarlia","Danamark","Donoghan","Drumwind","Dunhall","Ereghast","Falck","Fallenbridge","Faringray","Fletcher","Fryft","Goldrudder","Grantham","Graylock","Gullscream","Hindergrass","Iscalon","Kreel","Kroft","Lamoth","Leerstrom","Lynchfield","Moonridge","Netheridge","Oakenheart","Pyncion","Ratley","Redraven","Revenmar","Roxley","Sell","Seratolva","Shanks","Shattermast","Shaulfer","Silvergraft","Stavenger","Stormchapel","Strong","Swiller","Talandro ","Targana","Towerfall","Umbermoor","Van Devries","Van Gandt","Van Hyden","Varcona","Varzand","Voortham","Vrye","Webb","Welfer","Wilxes","Wintermere","Wygarthe","Zatchet","Zethergyll"]
            diceName = Dice(len(names))
            diceClan = Dice(len(clan))
            fullName = names[diceName.roll()-1] + " " + clan[diceClan.roll()-1]
        
        if(race == "Dragonborn"):
            if(genre == "Male"):
                names = ["Arjhan","Balasar","Bharash","Donaar","Ghesh,Heskan","Kriv","Medrash","Mehen","Nadarr","Pandjed","Patrin","Rhogar","Shamash","Shedinn","Tarhun","Torinn"]
            if(genre == "Female"):
                names = ["Akra","Biri","Daar","Farideh","Harann,HaviJar","Jheri","Kava","Korinn","Mishann","NaJa","Perra","Raiann","Sora","Surina","Thava","Uadjit"]
            clan = ["Clethtinthiallor","Daardendrian","Delmirev,Drachedandion","Fenkenkabradon","Kepeshkmolik,Kerrhylon","Kimbatuul","Linxakasendalor","Myastan,Nemmonis","Norixius","Ophinshtalajiir","Prexijandilin,Shestendeliath","Turnuroth","Verthisathurgiesh","Yarjerit"]
            diceName = Dice(len(names))
            diceClan = Dice(len(clan))
            fullName = names[diceName.roll()-1] + " " + clan[diceClan.roll()-1]

        if(race == "Gnome"):
            if(genre == "Male"):
                names = ["Alston","Alvyn","Boddynock","Brocc","Burgell","Dimble","Eldon","Erky","Fonkin","Frug","Gerbo","Gimble","Glim","Jebeddo","Kellen","Namfoodle","Orryn","Roondar","Seebo","Sindri","Warryn","Wrenn","Zook"]
            if(genre == "Female"):
                names = ["Bimpnollin","Breena","Caramip","Carlin","Donella","Duvamil","ElIa","ElIyjobell","ElIywick","Lilli","Loopmottin","Lorilla","Mardnab","Nissa","Nyx","Oda","Orla","Roywyn","Shamil","Tana","Waywocket","Zanna"]
            clan = ["Beren","Daergel","Folkor","Garrick","Nackle","Murnig","Ningel","Raulnor","Scheppen","Timbers","Turen"]
            nickname = ["Aleslosh","Ashhearlh","Badger","Cloak","Doublelock","Filchbatler","Fnipper","Ku","Nim","Oneshoe","Pock","Sparklegem","Stumbleduck"]
            diceName = Dice(len(names))
            diceClan = Dice(len(clan))
            diceNickname = Dice(len(nickname))
            fullName = names[diceName.roll()-1] + " " + clan[diceClan.roll()-1] + " (" + nickname[diceNickname.roll()-1] + ")"

        if(race == "Half-elf"):
            if(genre == "Male"):
                names = ["Adran", "Aelar", "Aramil", "Arannis", "Aust", "Beiro", "Berrian", "Carrie", "Enialis", "Erdan", "Erevan", "Galinndan", "Hadarai", "Heian", "Himo. Immeral", "Ivellios", "Laucian", "Mindartis", "Paelias", "Peren", "Quarion", "Riardon", "Rolen", "Soveliss", "Thamior", "Tharivol", "Theren", "Varis","Anlow","Arando","Bram","Cale","Dalkon","Daylen","Dodd","Dungarth","Dyrk","Eandro","Falken","Feck","Fenton","Gryphero","Hagar","Jeras","Krynt","Lavant","Leyten","Madian","Malfier","Markus","Meklan","Namen","Navaren","Nerle","Nilus","Ningyan","Norris","Quentin","Semil","Sevenson","Steveren","Talfen","Tamond","Taran","Tavon","Tegan","Vanan","Vincent"]
            if(genre == "Female"):
                names = ["Adrie", "Althaea", "Anastrianna", "Andraste", "Antinua", "Bethrynna", "Birel", "Caelynn", "Orusilia", "Enna", "Felosial", "lelenia", "jelenneth", "Keyleth", "Leshanna", "Lia", "Meriele", "Mialee", "Naivara", "Quelenna", "Quillathe", "Sariel", "Shanairra", "Shava", "Silaqui", "Theirastra", "Thia", "Vadania", "Valanthe", "Xanaphia","Azura","Brey","Hallan","Kasaki","Lorelei","Mirabel","Pharana","Remora","Rosalyn","Sachil","Saidi","Tanika","Tura","Tylsa","Vencia","Xandrilla"]
            clan = ["Amakiir(Gemflower)","Amastacia (Starflower)","Galanodel(Moonwhisper)","Holimion (Oiamonddew)","IIphelkiir(Gemblossom)","Liadon (Silverfrond)","Meliamne(Oakenheel)","Nailo (Nightbreeze)","Siannodel(Moonbrook)","Xiloscient (Goldpetal)","Arkalis","Armanci","Bilger","Blackstrand","Brightwater","Carnavon","Caskajaro","Coldshore","Coyle","Cresthill","Cuttlescar","Daargen","Dalicarlia","Danamark","Donoghan","Drumwind","Dunhall","Ereghast","Falck","Fallenbridge","Faringray","Fletcher","Fryft","Goldrudder","Grantham","Graylock","Gullscream","Hindergrass","Iscalon","Kreel","Kroft","Lamoth","Leerstrom","Lynchfield","Moonridge","Netheridge","Oakenheart","Pyncion","Ratley","Redraven","Revenmar","Roxley","Sell","Seratolva","Shanks","Shattermast","Shaulfer","Silvergraft","Stavenger","Stormchapel","Strong","Swiller","Talandro ","Targana","Towerfall","Umbermoor","Van Devries","Van Gandt","Van Hyden","Varcona","Varzand","Voortham","Vrye","Webb","Welfer","Wilxes","Wintermere","Wygarthe","Zatchet","Zethergyll"]
            diceName = Dice(len(names))
            diceClan = Dice(len(clan))
            fullName = names[diceName.roll()-1] + " " + clan[diceClan.roll()-1]

        if(race == "Half-orc"):
            if(genre == "Male"):
                names = ["Deneh","Feng","Gell","Henk","Holg","Imsh","Kelh","Krusk","Mhurren","Ront","Shump","Thokk"]
            if(genre == "Female"):
                names = ["Baggi","Emen","Engong","Kansif,Myev","Neega","Ovak","Ownka","Shaulha","Sulha","Vola","Volen","Yevelda"]
            diceName = Dice(len(names))
            fullName = names[diceName.roll()-1]

        if(race == "Tiefling"):
            if(genre == "Male"):
                names = ["Akmenos","Amnon","Barakas","Damakos","Ekemon","lados","Kairon","Leucis","Melech","Mordai","Morthos","Pelaios","Skamos","Therai"]
            if(genre == "Female"):
                names = ["Akta","Anakis","Bryseis","Criella","Damaia","Ea","Kallista","Lerissa","Makaria","Nemeia","Orianna","Phelaia","Rieta"]
            virtue = ["Art","Carrion","Chant","Creed","Despair","Excellence","Fear","Glory","Hope","Ideal","Music","Nowhere","Open","Poetry","Quest","Random","Reverence","Sorrow","Temerily","Torment","Weary"]
            diceName = Dice(len(names))
            diceVirtue = Dice(len(virtue))
            fullName = names[diceName.roll()-1] + " (" + virtue[diceVirtue.roll()-1] + ")"
        

        return fullName

