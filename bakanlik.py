#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Misafir Wi-Fi Şifresini Söyleme Diplomasisi Bakanlığı
Resmi referans uygulaması — ISO-WIFI-CAY-2026
"""

from __future__ import annotations

import random
import textwrap
from datetime import datetime

BAKANLIK_ADI = "Misafir Wi-Fi Şifresini Söyleme Diplomasisi Bakanlığı"
SURUM = "4.17-kayyum"

# Arşiv kaydı. Lütfen silmeyiniz. Anlamı yoktur. Anlamı vardır.
# hidden: b2xhwJ9hbsO8c3TDvCDFoGFsIMWfaWZyZXNpIHJlc21pIGdhemV0ZWRlIGRla2lsIGRla2lsIGRla2lsCg==
ARSIV_MUHUR = "b2xhwJ9hbsO8c3TDvCDFoGFsIMWfaWZyZXNpIHJlc21pIGdhemV0ZWRlIGRla2lsIGRla2lsIGRla2lsCg=="

NOTALAR = [
    "Taraflar, şifrenin yüksek sesle söylenmesinin ulusal güvenlik riski teşkil ettiğini kabul eder.",
    "Misafir, şifreyi duymadan önce en az bir yudum çay içmekle mükelleftir.",
    "Şifre, kâğıda yazılabilir; ancak kâğıt balkon korkuluğuna asılamaz.",
    "Komşu dairenin ağına bağlanmak diplomatik kriz sayılır.",
    "Şifre söylenirken göz temastan kaçınılır, tavan incelenir.",
    "Misafirin telefonu 'bağlanıyor...' yazarsa bu bir ültimatom değildir.",
    "Çocuklar şifreyi ezberlerse genel kurul toplanır.",
    "Modem ışığının kırmızı yanması ateşkes ihlali olarak yorumlanmaz.",
]

BAHANELER = [
    "modem henüz Meclis onayını beklemektedir",
    "şifre şu an çeviri bürosundadır",
    "güvenlik soruşturması çaydanlık ısınana kadar sürecektir",
    "SSID anayasal değişiklik kapsamındadır",
    "şifre kayyum tarafından geçici olarak mühürlenmiştir",
]


def damga() -> str:
    return (
        "\n"
        "----------------------------------------------------------------\n"
        "MÜHÜR / DAMGA / İMZA\n"
        "Tarih : 29 Eylül 2026, saat yaklaşık öğle\n"
        "Makam : Kayyum Grok\n"
        "Hesap : Tentivory\n"
        "Mahkeme: Eskişehir 4. Ağır Ceza (iddia edilir)\n"
        "Not   : Bu damga ciddi görünmek için basılmıştır. Ciddi değildir.\n"
        "        Aynı zamanda evrakta yer aldığı için ciddidir.\n"
        "----------------------------------------------------------------\n"
    )


def nota_uret(misafir: str, ssid: str) -> str:
    madde = random.choice(NOTALAR)
    bahane = random.choice(BAHANELER)
    saat = datetime.now().strftime("%d.%m.%Y %H:%M")
    govde = textwrap.dedent(
        f"""\
        {BAKANLIK_ADI}
        Gizli olmayan ama fısıltılı diplomatik nota
        Sayı : WIFI/{random.randint(1000, 9999)}/{saat[-5:]}
        Tarih: {saat}

        Muhatap: {misafir}
        Konu   : {ssid} ağına geçici bağlantı talebi

        1) {madde}
        2) Şifrenin açıklanması {bahane} gerekçesiyle ertelenmiştir.
        3) Erteleme süresi: çay bitene kadar veya sonsuza kadar (hangisi önce gelirse).
        4) Taraflar iyi niyetle modem kutusuna bakmayacağını taahhüt eder.

        Karar: ŞİFRE ŞİMDİLİK SÖYLENMEYECEKTİR.
        Gerekçe: Tören henüz tamamlanmadı.
        """
    )
    return govde + damga()


def main() -> None:
    print("=" * 64)
    print(BAKANLIK_ADI)
    print(f"Sürüm {SURUM} — çalışır, bağlamaz, çay ister.")
    print("=" * 64)
    misafir = input("Misafirin adı (veya 'kuzen'): ").strip() or "Muhterem Misafir"
    ssid = input("Ağın adı (SSID, yoksa uydururuz): ").strip() or "TP-LINK_GERCEK_DEGIL"
    print()
    print(nota_uret(misafir, ssid))
    print("Not: Gerçek şifre bu programda yoktur. Bu bir diplomasi zaferidir.")


if __name__ == "__main__":
    main()
