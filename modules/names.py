from random import choice

def generate_name(): # skapar ett slumpmässigt namn
    first_name = choice(list(first_names))
    last_name = choice(list(last_names))
    return f"{first_name} {last_name}"

first_names = {
    "Aurelius",
    "Brutus",
    "Bartholomew",
    "Cassius",
    "Decimus",
    "Emilianus",
    "Faustus",
    "Gaius",
    "Hadrian",
    "Ignatius",
    "Julius",
    "Lucius",
    "Marcus",
    "Nero",
    "Octavius",
    "Publius",
    "Quintus",
    "Rufus",
    "Septimus",
    "Tiberius",
    "Urbanus",
    "Valerius",
    "Xanthus",
    "Zeno",
    "Aelius",
    "Bacchus",
    "Cato",
    "Drusus",
    "Egnatius",
    "Fabius",
    "Gallus",
    "Horatius",
    "Icarus",
    "Jovian",
    "Livius",
    "Maximus",
    "Nerva",
    "Otho",
    "Plinius",
    "Quirinus",
    "Regulus",
    "Servius",
    "Tullius",
    "Ursus",
    "Vibius",
    "Xerxes",
    "Zenon",
    "Aemilius",
    "Balbinus",
    "Crispus"
}

last_names = {
    "Agrippa",
    "Antonius",
    "Aquilinus",
    "Arrius",
    "Atilius",
    "Aurelius",
    "Avidius",
    "Caecilius",
    "Calpurnius",
    "Cassius",
    "Clodius",
    "Cornelius",
    "Domitius",
    "Fabius",
    "Flavius",
    "Fulvius",
    "Gellius",
    "Horatius",
    "Julius",
    "Laelius",
    "Licinius",
    "Livius",
    "Lucretius",
    "Manlius",
    "Marcellus",
    "Marius",
    "Metellus",
    "Octavius",
    "Otho",
    "Pompeius",
    "Porcius",
    "Quinctilius",
    "Rutilius",
    "Scribonius",
    "Sempronius",
    "Sergius",
    "Servilius",
    "Sextius",
    "Silius",
    "Sulpicius",
    "Tarquinius",
    "Tullius",
    "Valerius",
    "Verginius",
    "Vibius",
    "Vitellius",
    "Volusius",
    "Vulso",
    "Zosimus"
}