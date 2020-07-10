class Czso:
    """Class for mapping API resources of Czech Statistical Office, provided by Apitalks.

    References:
        https://www.api.store/czso.cz/dokumentace (in czech language)
    """

    lide_domy_byty = "/czso.cz/lide-domy-byty"
    vyjizdky_zamestnani = "/czso.cz/vyjizdky-zamestnani"
    obyvatele_sidelni_jednotky = "/czso.cz/obyvatele-sidelni-jednotky"
    obyvatelstvo_domy = "/czso.cz/obyvatelstvo-domy"
    prumerne_mzdy_odvetvi = "/czso.cz/prumerne-mzdy-odvetvi"
    cizinci_dle_obcanstvi_veku_pohlavi = (
        "/czso.cz/cizinci-podle-statniho-obcanstvi-veku-a-pohlavi"
    )
    pohyb_obyvatel = "/czso.cz/pohyb-obyvatel-za-cr-kraje-okresy-so-orp-a-obce"
    nadeje_doziti = "/czso.cz/nadeje-doziti-v-okresech-a-spravnich-obvodech-orp"
    prumerne_spotrebitelske_ceny = (
        "/czso.cz/prumerne-spotrebitelske-ceny-vybranych-vyrobku-potravinarske-vyrobky"
    )
    hoste_a_prenocovani = (
        "/czso.cz/hoste-a-prenocovani-v-hromadnych-ubytovacich-zarizenich-podle-zemi"
    )
    ciselniky_obce_a_ujezdy = "/czso.cz/obec-a-vojensky-ujezd"
    ciselniky_mestske_obvody_a_casti = "/czso.cz/mestsky-obvod-mestska-cast"
    ciselniky_spr_obv_s_rozsirenou_pusobnosti = (
        "/czso.cz/spravni-obvody-obci-s-rozsirenou-pusobnosti"
    )
    ciselniky_spr_obv_praha = "/czso.cz/spravni-obvod-v-hlavnim-meste-praze"
    ciselniky_stat = "/czso.cz/stat"
    ciselniky_region_soudrznosti = "/czso.cz/region-soudrznosti"
    ciselniky_kraj = "/czso.cz/kraj"
    ciselniky_okres = "/czso.cz/okres"

    def __init__(self) -> None:
        pass


class CzechPost:
    """Class for mapping API resources of Czech Post Office, provided by Apitalks.

    References:
        https://www.api.store/ceskaposta.cz/dokumentace (in czech language)
    """

    provozovny = "/cpost.cz/provozovny"
    posty_info = "/cpost.cz/posty"
    postovni_schranky = "/cpost.cz/postovni-schranky"
    psc = "/cpost.cz/psc"
    mista_bez_dorucovani = "/cpost.cz/bez-dorucovani"
    psc_s_dorucovacim_pasmem = "/cpost.cz/psc-s-dorucovacim-pasmem"
    psc_adresni = "/cpost.cz/adresni-psc"
    obce_s_adresni_psc = "/cpost.cz/obce-adresni-psc"
    provozovny_s_baliky = "/cpost.cz/provozovny-balik"
    provozovny_s_baliky_nad_30kg = "/cpost.cz/provozovny-balik-30kg"
    mista_zkracene_dodani = "/cpost.cz/mista-zkracene-dodani"
    mista_zkracene_dodani_svatky = "/cpost.cz/mista-zkracene-dodani-svatky"
    mista_prevzeti_u_odesilatele = "/cpost.cz/mista-prevezeti-u-odesilatele"
    provozovny_podat_balik_na_postu = "/cpost.cz/podani-baliku-na-postu"
    provozovny_ulozit_balik_na_postu = "/cpost.cz/adresovani-baliku-na-postu"
    balikovny = "/cpost.cz/balikovny"
    adresovani_balik_expres = "/cpost.cz/adresovani-baliku-expres"
    podani_balik_expres = "/cpost.cz/podani-baliku-expres"
    podani_balik_nadrozmer = "/cpost.cz/podani-baliku-nadrozmer"
    ulozit_balik_nadrozmer = "/cpost.cz/ulozeni-baliku-nadrozmer"
    roznasky_propagacnich_materialu_pocty = "/cpost.cz/pocty-RIPM"
    roznasky_propagacnich_materialu_posty = "/cpost.cz/objednavka-RIPM"

    def __init__(self) -> None:
        pass


class DataBoxes:
    """Class for mapping API resources of Data Boxes (Datove schranky), provided by Apitalks.

    References:
        https://www.api.store/datove-schranky/ (in czech language)
    """

    datove_schranky = "/datove-schranky"

    def __init__(self) -> None:
        pass


class HealthServices:
    """Class for mapping API resources of Health Service (Zdravotni sluzby), provided by Apitalks.

    References:
        https://www.api.store/zdravotni-sluzby/ (in czech language)
    """

    zdravotni_sluzby = "/zdravotni-sluzby"

    def __init__(self) -> None:
        pass


class CzechBusinessInspection:
    """Class for mapping API resources of Czech Business Inspection (Ceska obchodni inspekce), provided by Apitalks.

    References:
        https://www.api.store/coi/ (in czech language)
    """

    rizikove_weby = "/coi/rizikove-weby"
    sankce = "/coi/sankce"
    zajisteni = "/coi/zajisteni"
    zakazy = "/coi/zakazy"
    zamereni = "/coi/zamereni"

    def __init__(self) -> None:
        pass


class Schools:
    """Class for mapping API resources of schools provided by Apitalks.

    References:
        https://www.api.store/skoly/ (in czech language)
    """

    skoly = "/skoly"

    def __init__(self) -> None:
        pass


