import re
import unicodedata

def validate_label(label):
    label = unicodedata.normalize('NFKC', label)

    if re.search(r"[0-9]", label) is not None:
        return None

    if '*' in label:
        return None

    skip_foreign_chars = [
        'ʔ',
        'ε',
        'ι',
        'ο',
        'ό',
        'ρ',
        'ς',
        'ψ',
        'գ',
        'զ',
        'ا',
        'ب',
        'د',
        'ر',
        'ل',
        'ن',
        'و',
        'ي',
        'ቀ',
        'ወ',
        'う',
        'ゔ',
        'へ',
        'ま',
        'め',
        'や',
        '貴',
        '青',
        'い',
        'た',
        'つ',
        'ぬ',
        'の',
        '乃',
        '京',
        '北',
        '扬',
        '星',
        '术',
        '杜',
        '美',
        '馆',
        '삼',
        '고',
        '생',
        '기',
        '집',
        '먹',
        '西',
        '甌',
        '牡',
        '文',
        '丹',
        'も', 
        'む',
        'ⱅ', #<-- comment me when people stop thinking i'm a m
        'ⱎ', #<-- comment me when people stop thinking i'm a w
        'ጀ',
        'ከ',
        'ӌ',
        'є',
        'э',
        'ч',
        'ц',
        'р̌',
        'р',
        '◌̌',
        'п', #<-- comment me when people stop thinking i'm Pi
        'л',
        'д',
        'χ', #<-- comment me if someone can pronounce me correctly /xi/
        'λ', #<-- comment me when everyone knows how to pronounce |λ|
        'η', #<-- comment me when people know my name is êta
        'ɨ' ,#<-- comment me when everyone stop thinking i'm a t
        'ꝑ', #<-- comment me when people can lookup my name
        'ɛ',
        'ə',
        'ɔ',
    ]

    for skip in skip_foreign_chars:
        if skip in label:
            return None

    label = label.strip()
    label = label.lower()

    label = label.replace("宇津保", "utsuho")
    label = label.replace("厳", "")
    label = label.replace("三", "")
    label = label.replace("⊨", "inclus")

    label = label.replace("ⱅ", "m") #<-- comment me when people stop thinking i'm a m
    label = label.replace("ⱎ", "w") #<-- comment me when people stop thinking i'm a w
    label = label.replace("р", "p") #<-- comment me when people stop thinking i'm a p
    
    label = label.replace("=", "")
    label = label.replace("|", "")
    label = label.replace("-", " ")
    label = label.replace("–", " ")
    label = label.replace("—", " ")
    label = label.replace("’", " ")
    label = label.replace("ʽ", " ")
    label = label.replace('’', "'")
    label = label.replace("^", "e")
    #label = label.replace("'", " ")
    label = label.replace("º", "degré")
    label = label.replace("…", " ")
    label = label.replace("_", " ")
    label = label.replace(".", "")
    label = label.replace(",", "")
    label = label.replace("?", "")
    label = label.replace("!", "")
    label = label.replace("\"", "")
    label = label.replace("(", "")
    label = label.replace(")", "")
    label = label.replace("{", "")
    label = label.replace("}", "")
    label = label.replace("/", " ")
    label = label.replace(":", "")
    label = label.replace(";", "")
    label = label.replace("«", "")
    label = label.replace("»", "")
    label = label.replace("%", "")
    label = label.replace("`", "")
    label = label.replace("°", "degré")
    label = label.replace("+", "plus")
    label = label.replace("±", "plus ou moins")
    label = label.replace("·", "")
    label = label.replace("×", "")
    label = label.replace("∼", "~")
    label = label.replace("̐", "")
    label = label.replace("─", "")
    label = label.replace("̲", "")


    label = label.replace("ă", "a")
    label = label.replace("ắ", "a")
    label = label.replace("ầ", "a")
    label = label.replace("å", "a")
    label = label.replace("ä", "a")
    label = label.replace("ą", "a")
    label = label.replace("ā", "a")
    label = label.replace("ả", "a")
    label = label.replace("ạ", "a")
    label = label.replace("ậ", "a")
    #label = label.replace("æ", "")
    label = label.replace("ć", "c")
    label = label.replace("č", "c")
    label = label.replace("ċ", "c")
    label = label.replace("đ", "d")
    label = label.replace("ḍ", "d")
    label = label.replace("ð", "o")
    label = label.replace("ễ", "e")
    label = label.replace("ě", "e")
    label = label.replace("ė", "e")
    label = label.replace("ę", "e")
    label = label.replace("ē", "e")
    label = label.replace("ệ", "e")
    label = label.replace("ğ", "g")
    label = label.replace("ġ", "g")
    label = label.replace("ħ", "h")
    label = label.replace("ʻ", "")
    label = label.replace("ì", "i")
    label = label.replace("ī", "i")
    label = label.replace("ị", "")
    label = label.replace("ı", "un")
    label = label.replace("ľ", "l'")
    label = label.replace("ļ", "l")
    label = label.replace("ł", "")
    label = label.replace("ǹ", "n")
    label = label.replace("ň", "n")
    label = label.replace("ṅ", "n")
    label = label.replace("ņ", "n")
    label = label.replace("ṇ", "n")
    label = label.replace("ŏ", "o")
    label = label.replace("ồ", "o")
    label = label.replace("ổ", "o")
    label = label.replace("ő", "o")
    label = label.replace("õ", "o")
    label = label.replace("ø", "o")
    label = label.replace("ǫ", "o")
    label = label.replace("ơ", "")
    label = label.replace("ợ", "")
    label = label.replace("ộ", "o")
    label = label.replace("ř", "r")
    label = label.replace("ś", "s")
    label = label.replace("š", "s")
    label = label.replace("ş", "s")
    label = label.replace("ṣ", "s")
    label = label.replace("ș", "s")
    label = label.replace("ß", "ss")
    label = label.replace("ť", "t")
    label = label.replace("ṭ", "t")
    label = label.replace("ț", "t")
    label = label.replace("ṯ", "t")
    label = label.replace("ú", "u")
    label = label.replace("ų", "u")
    label = label.replace("ư", "u")
    label = label.replace("ử", "u")
    label = label.replace("ʉ", "")
    label = label.replace("ý", "y")
    label = label.replace("ỳ", "y")
    label = label.replace("ź", "z")
    label = label.replace("ž", "z")
    label = label.replace("ż", "z")
    label = label.replace("þ", "")
    label = label.replace("ʼ", "")
    label = label.replace("ʾ", "")
    label = label.replace("ʿ", "")
    label = label.replace("ǃ", "")
    label = label.replace("δ", "delta")
    label = label.replace("ζ", "")
    label = label.replace("κ", "kappa")
    label = label.replace("ν", "")
    label = label.replace("π", "pi")
    label = label.replace("σ", "sigma")
    label = label.replace("τ", "tau")
    label = label.replace("υ", "")
    label = label.replace("ω", "omega")
    label = label.replace("а", "a")
    label = label.replace("г", "r")
    label = label.replace("е", "e")
    label = label.replace("з", "")
    label = label.replace("и", "")
    label = label.replace("к", "")
    label = label.replace("м", "")
    label = label.replace("н", "")
    label = label.replace("ҫ", "c")
    label = label.replace("я", "")
    label = label.replace("א", "")
    label = label.replace("ደ", "")
    label = label.replace("ጠ", "")
    label = label.replace("ķ", "k")
    label = label.replace("ǀ", "")
    

    label = label.replace("α", "alpha")
    label = label.replace("γ", "gamma")
    label = label.replace("μ", "mu")

    label = label.replace("→", "")
    label = label.replace("↔", "")

    label = label.replace("‘", "")
    label = label.replace("“", "")
    label = label.replace("”", "")
    label = label.replace("„", "")
    label = label.replace("†", "")
    label = label.replace("′", "")
    label = label.replace("‹", "")
    label = label.replace("›", "")
    label = label.replace("⁄", "")
    label = label.replace("∅", "")
    label = label.replace("∈", "")
    label = label.replace("∞", "")
    label = label.replace("≥", "")
    label = label.replace("☉", "")
    label = label.replace("ː", "")
    label = label.replace("§", "paragraphe")
    label = label.replace("$", "dollars")
    label = label.replace("£", "livres")
    label = label.replace("€", "euros")
    #label = label.replace("₽", "rouble russe") #<-- if you need this currency
    label = label.replace("β", "beta")
    label = label.replace("σ", "gamma")
    label = label.replace("½", "demi")
    label = label.replace("¼", "quart")
    label = label.replace("&", "et")
    label = label.replace("æ", "é")
    label = label.replace("nºˢ", "numéros")
    label = label.replace("nº", "numéro")
    label = label.replace("n°", "numéro")
    label = label.replace("         ", " ")
    label = label.replace("        ", " ")
    label = label.replace("       ", " ")
    label = label.replace("      ", " ")
    label = label.replace("     ", " ")
    label = label.replace("    ", " ")
    label = label.replace("   ", " ")
    label = label.replace("  ", " ")

    label = label.replace(u"\u0301", "")
    label = label.replace(u"\u0307", "")
    label = label.replace(u"\u0320", "")
    label = label.replace(u"\u0331", "")

    label = label.strip()
    label = label.lower()

    return label if label else None
