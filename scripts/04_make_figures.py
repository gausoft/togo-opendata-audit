"""Generate the report figures from real audit data, in FR or EN.

Style: dark theme matching gausoft.dev (near-black bg, orange accent,
cyan good-performer accent, off-white ink). Thin lines, generous
whitespace, minimal chartjunk.

Usage:
    python scripts/04_make_figures.py            # FR (default)
    python scripts/04_make_figures.py --lang en  # EN, outputs *_en.png

Outputs (FR):
  reports/figures/fig1_ministry_schema_only.png
  reports/figures/fig2_freshness_wall.png
  reports/figures/fig3_creation_timeline.png

Outputs (EN):
  reports/figures/fig1_ministry_schema_only_en.png
  reports/figures/fig2_freshness_wall_en.png
  reports/figures/fig3_creation_timeline_en.png
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import font_manager

# Register Sora (gausoft.dev brand font) if installed locally
for _p in (Path.home() / "Library/Fonts/Sora.ttf", Path("/Library/Fonts/Sora.ttf")):
    if _p.exists():
        font_manager.fontManager.addfont(str(_p))
        break
_FONT = "Sora" if any(f.name == "Sora" for f in font_manager.fontManager.ttflist) else "DejaVu Sans"

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "reports" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

# --- design tokens (gausoft.dev charter) ------------------------------------
BG = "#09090B"
PANEL = "#18181B"
INK = "#FAFAFA"
INK_SOFT = "#A1A1AA"
INK_FAINT = "#52525B"
ACCENT = "#EA580C"
ACCENT_2 = "#FB923C"
GOOD = "#06B6D4"

mpl.rcParams.update({
    "font.family": _FONT,
    "font.size": 11,
    "text.color": INK,
    "axes.edgecolor": INK_FAINT,
    "axes.labelcolor": INK,
    "xtick.color": INK_SOFT,
    "ytick.color": INK_SOFT,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.spines.left": False,
    "axes.spines.bottom": True,
    "figure.facecolor": BG,
    "axes.facecolor": BG,
    "savefig.facecolor": BG,
    "savefig.dpi": 200,
})


# --- i18n strings -----------------------------------------------------------
STR = {
    "fr": {
        # fig 1
        "f1_title": "Part de fichiers vides par ministère togolais",
        "f1_subtitle": "% de la première ressource CSV ne contenant que la liste des colonnes, sans données",
        "f1_threshold": " seuil 50 %",
        "f1_caption": (
            "Lecture · Trois ministères publient à 100 % des fichiers vides ; trois autres à 100 % des données réelles.\n"
            "Le nombre entre parenthèses indique le total de datasets publiés par chaque ministère."
        ),
        "f1_source": "Source : audit indépendant · gausoft/togo-opendata-audit · mai 2026",
        "f1_suffix_total": "",  # already inline " (N)"
        # fig 2
        "f2_title": "Quand les 1 550 datasets ont-ils été modifiés pour la dernière fois ?",
        "f2_subtitle": "Distribution de la date last_modified, mesurée en mai 2026",
        "f2_buckets": ["< 1 mois", "1–3 mois", "3–6 mois", "6–12 mois", "12–24 mois", "> 24 mois"],
        "f2_caption": (
            "Lecture · 99,7 % des datasets ont été touchés pour la dernière fois entre décembre 2024 et mai 2025,\n"
            "puis le portail s’est arrêté. Aucun dataset n’a été modifié dans les 6 derniers mois."
        ),
        "f2_source": "Source : /api/1/datasets/ · gausoft/togo-opendata-audit · mai 2026",
        # fig 3
        "f3_title": "Quand les 1 550 datasets ont-ils été créés ?",
        "f3_subtitle": "Nombre de datasets créés par mois sur opendata.gouv.tg, novembre 2024 – mai 2026",
        "f3_months": ["jan", "fév", "mar", "avr", "mai", "juin",
                      "juil", "août", "sep", "oct", "nov", "déc"],
        "f3_burst_label": "5 mois de « rafale »\n{n} datasets créés",
        "f3_silence_label": "7 mois de silence\n(novembre 2025 – mai 2026)",
        "f3_caption": (
            "Lecture · 99,9 % des datasets ont été créés lors d’une rafale initiale de cinq mois (décembre 2024 – mars 2025).\n"
            "Le portail n’a quasiment plus rien créé depuis. C’est la signature d’une livraison de projet, pas d’un service continu."
        ),
        "f3_source": "Source : champ created_at de /api/1/datasets/ · gausoft/togo-opendata-audit · mai 2026",
    },
    "en": {
        # fig 1
        "f1_title": "Share of empty files per Togolese ministry",
        "f1_subtitle": "% of first CSV resources containing only the column list, with no data",
        "f1_threshold": " 50% threshold",
        "f1_caption": (
            "How to read · Three ministries publish 100% empty files; three others publish 100% real data.\n"
            "The number in parentheses is the total dataset count for each ministry."
        ),
        "f1_source": "Source: independent audit · gausoft/togo-opendata-audit · May 2026",
        "f1_suffix_total": "",
        # fig 2
        "f2_title": "When were the 1,550 datasets last modified?",
        "f2_subtitle": "Distribution of last_modified dates, measured in May 2026",
        "f2_buckets": ["< 1 month", "1–3 months", "3–6 months", "6–12 months", "12–24 months", "> 24 months"],
        "f2_caption": (
            "How to read · 99.7% of datasets were last touched between December 2024 and May 2025,\n"
            "then the portal stopped. No dataset has been modified in the past 6 months."
        ),
        "f2_source": "Source: /api/1/datasets/ · gausoft/togo-opendata-audit · May 2026",
        # fig 3
        "f3_title": "When were the 1,550 datasets created?",
        "f3_subtitle": "Datasets created per month on opendata.gouv.tg, November 2024 – May 2026",
        "f3_months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                      "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "f3_burst_label": "5-month burst\n{n} datasets created",
        "f3_silence_label": "7 months of silence\n(November 2025 – May 2026)",
        "f3_caption": (
            "How to read · 99.9% of datasets were created during a five-month initial burst (December 2024 – March 2025).\n"
            "The portal has produced almost nothing since. This is the signature of a project delivery, not of a running service."
        ),
        "f3_source": "Source: created_at field from /api/1/datasets/ · gausoft/togo-opendata-audit · May 2026",
    },
}

# Ministry short labels: keep FR institutional names (proper nouns of Togolese
# administrations) but add EN-friendly forms for the English chart.
SHORT_FR = {
    "Ministère des Armées": "Armées",
    "Ministère de la Sécurité et de la Protection Civile": "Sécurité & Protection Civile",
    "Ministère de l'Économie Numérique et de la Transformation Digitale": "Économie Numérique",
    "Ministère de l’Enseignement Supérieur et de la Recherche": "Enseignement Supérieur",
    "Ministère du Commerce, de l'Artisanat et de la Consommation Locale": "Commerce & Artisanat",
    "Ministère des Transports": "Transports",
    "Ministère de  l’Accès Universel aux Soins et de la Couverture Sanitaire": "Santé (Accès Universel)",
    "Ministère de l'Environnement et des Ressources Forestières": "Environnement",
    "Ministère de l’Enseignement Technique, de la Formation Professionnelle et de l’Apprentissage": "Enseignement Technique",
    "Ministère de l'Enseignement Primaire et Secondaire": "Enseignement Primaire",
    "Ministère des Sports et des Loisirs": "Sports & Loisirs",
    "Ministère du Tourisme": "Tourisme",
    "Ministère de l’Eau et de l’Assainissement": "Eau & Assainissement",
    "Ministère de l'Économie et des Finances": "Économie & Finances",
    "Ministère de l’Action Sociale, de la Solidarité et de la Promotion de la Femme": "Action Sociale",
    "Ministère de l'Agriculture, de l’Hydraulique  et du Développement Rural": "Agriculture",
    "Ministère des Travaux Publics et des Infrastructures": "Travaux Publics",
    "Ministère de la Planification du Développement et de la Coopération": "Planification",
}

SHORT_EN = {
    "Ministère des Armées": "Defence",
    "Ministère de la Sécurité et de la Protection Civile": "Security & Civil Protection",
    "Ministère de l'Économie Numérique et de la Transformation Digitale": "Digital Economy",
    "Ministère de l’Enseignement Supérieur et de la Recherche": "Higher Education",
    "Ministère du Commerce, de l'Artisanat et de la Consommation Locale": "Trade & Crafts",
    "Ministère des Transports": "Transport",
    "Ministère de  l’Accès Universel aux Soins et de la Couverture Sanitaire": "Health (Universal Access)",
    "Ministère de l'Environnement et des Ressources Forestières": "Environment",
    "Ministère de l’Enseignement Technique, de la Formation Professionnelle et de l’Apprentissage": "Technical Education",
    "Ministère de l'Enseignement Primaire et Secondaire": "Primary Education",
    "Ministère des Sports et des Loisirs": "Sports & Leisure",
    "Ministère du Tourisme": "Tourism",
    "Ministère de l’Eau et de l’Assainissement": "Water & Sanitation",
    "Ministère de l'Économie et des Finances": "Economy & Finance",
    "Ministère de l’Action Sociale, de la Solidarité et de la Promotion de la Femme": "Social Action",
    "Ministère de l'Agriculture, de l’Hydraulique  et du Développement Rural": "Agriculture",
    "Ministère des Travaux Publics et des Infrastructures": "Public Works",
    "Ministère de la Planification du Développement et de la Coopération": "Planning",
}


def _suffix(lang: str) -> str:
    return "_en" if lang == "en" else ""


def _fmt_thousands(n: int, lang: str) -> str:
    if lang == "en":
        return f"{n:,}"
    return f"{n:,}".replace(",", " ")


# =============================================================================
# Figure 1 — % of schema-only files per ministry
# =============================================================================
def figure_ministries(lang: str) -> None:
    s = STR[lang]
    short = SHORT_EN if lang == "en" else SHORT_FR

    data = json.loads((ROOT / "data" / "processed" / "content_audit.json").read_text())
    by_org = data["by_organization"]

    keep_keywords = ("Ministère",)
    rows = []
    for name, v in by_org.items():
        if not name.strip().startswith(keep_keywords):
            continue
        if v["total"] < 5:
            continue
        rows.append((name.strip(), v["total"], v["schema_only_pct"], v["real_data_pct"]))

    rows.sort(key=lambda r: -r[2])

    labels = [f"{short.get(name, name)}  ({total})" for name, total, _, _ in rows]
    schema_pct = [r[2] for r in rows]

    fig, ax = plt.subplots(figsize=(11, 9))

    y = list(range(len(rows)))
    colors = [ACCENT if p >= 1 else GOOD for p in schema_pct]
    ax.barh(y, schema_pct, color=colors, height=0.7, edgecolor="none")

    ax.axvline(50, color=INK_FAINT, linewidth=0.6, linestyle=(0, (3, 4)), zorder=0)
    ax.text(50, len(rows) - 0.2, s["f1_threshold"], color=INK_SOFT, fontsize=9, va="center")

    for i, p in enumerate(schema_pct):
        if p >= 5:
            ax.text(p - 1.5, i, f"{p:.0f}%", color="#FFFFFF", fontsize=10,
                    ha="right", va="center", fontweight="bold")
        else:
            ax.text(p + 1.5, i, f"{p:.0f}%", color=GOOD, fontsize=10,
                    ha="left", va="center", fontweight="bold")

    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=10, color=INK)
    ax.invert_yaxis()
    ax.set_xlim(0, 105)
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_xticklabels(["0%", "25%", "50%", "75%", "100%"], fontsize=10, color=INK_SOFT)
    ax.tick_params(axis="y", length=0)
    ax.tick_params(axis="x", length=0, pad=4)
    ax.spines["bottom"].set_color(INK_FAINT)
    ax.spines["bottom"].set_linewidth(0.6)

    fig.text(0.04, 0.965, s["f1_title"], fontsize=17, fontweight="bold", color=INK)
    fig.text(0.04, 0.935, s["f1_subtitle"], fontsize=11, color=INK_SOFT)
    fig.text(0.04, 0.05, s["f1_caption"], fontsize=9, color=INK_SOFT, style="italic")
    fig.text(0.04, 0.02, s["f1_source"], fontsize=8, color=INK_SOFT)

    plt.subplots_adjust(left=0.32, right=0.96, top=0.90, bottom=0.13)
    out = OUT / f"fig1_ministry_schema_only{_suffix(lang)}.png"
    fig.savefig(out, dpi=220, bbox_inches="tight", facecolor=BG)
    print(f"wrote {out}")
    plt.close(fig)


# =============================================================================
# Figure 3 — Dataset creation timeline
# =============================================================================
def figure_creation_timeline(lang: str) -> None:
    import collections, datetime as dt
    s = STR[lang]
    data = json.loads((ROOT / "data" / "raw" / "datasets_metadata.json").read_text())
    counts: collections.Counter = collections.Counter()
    for d in data:
        c = d.get("created_at") or d.get("created")
        if not c:
            continue
        t = dt.datetime.fromisoformat(c.replace("Z", "+00:00"))
        counts[(t.year, t.month)] += 1

    months = []
    y, m = 2024, 11
    while (y, m) <= (2026, 5):
        months.append((y, m))
        m += 1
        if m == 13:
            m, y = 1, y + 1

    values = [counts.get(k, 0) for k in months]
    short_months = s["f3_months"]
    labels = []
    for i, (yy, mm) in enumerate(months):
        if mm == 1 or i == 0:
            labels.append(f"{short_months[mm-1]}\n{yy}")
        else:
            labels.append(short_months[mm-1])

    fig, ax = plt.subplots(figsize=(13, 6))

    x = list(range(len(months)))
    colors = [ACCENT if v >= 50 else INK_FAINT for v in values]
    ax.bar(x, values, color=colors, width=0.7, edgecolor="none")

    for i, v in enumerate(values):
        if v >= 50:
            ax.text(i, v + 12, f"{v}", ha="center", color=INK,
                    fontsize=11, fontweight="bold")
        elif v > 0:
            ax.text(i, v + 12, f"{v}", ha="center", color=INK_SOFT, fontsize=9)

    burst_total = sum(v for v in values[:5])
    ax.annotate(
        s["f3_burst_label"].format(n=burst_total),
        xy=(2, 643), xytext=(2.2, 720),
        color=ACCENT, fontsize=10, fontweight="bold",
        arrowprops=dict(arrowstyle="-", color=ACCENT, lw=0.6, alpha=0.5),
    )
    ax.annotate(
        s["f3_silence_label"],
        xy=(16, 0), xytext=(13.5, 320),
        color=INK_SOFT, fontsize=10, style="italic",
        arrowprops=dict(arrowstyle="-", color=INK_SOFT, lw=0.6, alpha=0.5),
    )

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=9, color=INK_SOFT)
    ax.set_yticks([])
    ax.tick_params(axis="x", length=0, pad=4)
    ax.spines["bottom"].set_color(INK_FAINT)
    ax.spines["bottom"].set_linewidth(0.6)
    ax.set_ylim(0, max(values) * 1.25)

    fig.text(0.04, 0.95, s["f3_title"], fontsize=17, fontweight="bold", color=INK)
    fig.text(0.04, 0.905, s["f3_subtitle"], fontsize=11, color=INK_SOFT)
    fig.text(0.04, 0.04, s["f3_caption"], fontsize=9, color=INK_SOFT, style="italic")
    fig.text(0.04, 0.005, s["f3_source"], fontsize=8, color=INK_SOFT)

    plt.subplots_adjust(left=0.05, right=0.97, top=0.86, bottom=0.18)
    out = OUT / f"fig3_creation_timeline{_suffix(lang)}.png"
    fig.savefig(out, dpi=220, bbox_inches="tight", facecolor=BG)
    print(f"wrote {out}")
    plt.close(fig)


# =============================================================================
# Figure 2 — Freshness "wall"
# =============================================================================
def figure_freshness(lang: str) -> None:
    s = STR[lang]
    data = json.loads((ROOT / "data" / "processed" / "metadata_analysis.json").read_text())
    buckets = data["freshness_buckets"]

    order = ["< 1 month", "1-3 months", "3-6 months", "6-12 months",
             "12-24 months", "> 24 months"]
    bucket_labels = s["f2_buckets"]
    values = [buckets.get(k, 0) for k in order]

    fig, ax = plt.subplots(figsize=(11, 6))

    x = list(range(len(order)))
    colors = [INK_FAINT if v < 100 else ACCENT for v in values]
    ax.bar(x, values, color=colors, width=0.62, edgecolor="none")

    for i, v in enumerate(values):
        if v >= 50:
            ax.text(i, v + 30, _fmt_thousands(v, lang),
                    ha="center", color=INK, fontsize=12, fontweight="bold")
        elif v > 0:
            ax.text(i, v + 30, f"{v}", ha="center", color=INK_SOFT, fontsize=10)
        else:
            ax.text(i, 30, "0", ha="center", color=INK_FAINT, fontsize=10)

    ax.set_xticks(x)
    ax.set_xticklabels(bucket_labels, fontsize=11, color=INK)
    ax.set_yticks([])
    ax.tick_params(axis="x", length=0, pad=6)
    ax.spines["bottom"].set_color(INK_FAINT)
    ax.spines["bottom"].set_linewidth(0.6)
    ax.set_ylim(0, max(values) * 1.18)

    fig.text(0.05, 0.95, s["f2_title"], fontsize=17, fontweight="bold", color=INK)
    fig.text(0.05, 0.905, s["f2_subtitle"], fontsize=11, color=INK_SOFT)
    fig.text(0.05, 0.04, s["f2_caption"], fontsize=9, color=INK_SOFT, style="italic")
    fig.text(0.05, 0.005, s["f2_source"], fontsize=8, color=INK_SOFT)

    plt.subplots_adjust(left=0.06, right=0.96, top=0.86, bottom=0.18)
    out = OUT / f"fig2_freshness_wall{_suffix(lang)}.png"
    fig.savefig(out, dpi=220, bbox_inches="tight", facecolor=BG)
    print(f"wrote {out}")
    plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--lang", choices=["fr", "en"], default="fr",
                        help="Output language (default: fr). EN files get an _en suffix.")
    args = parser.parse_args()
    figure_ministries(args.lang)
    figure_freshness(args.lang)
    figure_creation_timeline(args.lang)
