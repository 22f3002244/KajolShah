from flask import Flask, render_template

app = Flask(__name__)

# ── Data ──────────────────────────────────────────────────────────────────────

LITIGATION_SERVICES = [
    {
        "title": "Criminal Defense Litigation",
        "desc":  "Bail, anticipatory bail, trials, appeals, and revisions before District Courts, High Courts, and the Supreme Court of India.",
    },
    {
        "title": "Cheque Bounce — S. 138 NI Act",
        "desc":  "Expert representation before Magistrate Courts and appellate forums across Mumbai, for both complainant and accused sides.",
    },
    {
        "title": "Civil Dispute Resolution",
        "desc":  "Property disputes, recovery suits, injunctions, and civil appeals — from filing to final decree execution.",
    },
    {
        "title": "Commercial & Corporate Litigation",
        "desc":  "Contract disputes, commercial fraud, partnership disagreements before commercial courts in Mumbai.",
    },
    {
        "title": "Consumer Protection Litigation",
        "desc":  "Representation before District Forums, State Commission, and NCDRC in deficiency of service matters.",
    },
    {
        "title": "Labour & Employment Law",
        "desc":  "Industrial disputes, wrongful termination, and workplace compliance before Labour Courts and Industrial Tribunals.",
    },
    {
        "title": "DRT & Debt Recovery",
        "desc":  "Specialised practice before DRT and DRAT Mumbai — OA filings, SA applications, and recovery proceedings.",
    },
    {
        "title": "NCLT / Insolvency & IBC",
        "desc":  "Representing creditors, debtors, and resolution professionals in insolvency and restructuring matters.",
    },
    {
        "title": "Arbitration & Conciliation",
        "desc":  "Domestic and international arbitration, conciliation, and mediation proceedings.",
    },
    {
        "title": "Family Law & Matrimonial",
        "desc":  "Divorce, maintenance, alimony, child custody, and guardianship before Family Courts and High Courts.",
    },
    {
        "title": "Cyber Crime & IT Act",
        "desc":  "Cyber fraud, online harassment, data theft, and IT Act offences before Mumbai Cyber Cell and criminal courts.",
    },
    {
        "title": "GST & Tax Litigation",
        "desc":  "Representation before GST Appellate Authorities, CESTAT, and High Courts in tax disputes.",
    },
]

NONLIT_SERVICES = [
    {
        "title": "Real Estate & RERA",
        "desc":  "Builder disputes, possession delays, and RERA complaints before MahaRERA.",
    },
    {
        "title": "Property Title Verification",
        "desc":  "Detailed title search and legal scrutiny reports for residential and commercial properties in Mumbai.",
    },
    {
        "title": "Deed Drafting & Registration",
        "desc":  "Sale Deeds, Lease Deeds, Leave & Licence Agreements, Gift Deeds, and Mortgage Deeds.",
    },
    {
        "title": "Business Agreement Drafting",
        "desc":  "Partnership Deeds, Shareholder Agreements, JV Agreements, Vendor Contracts, and NDAs.",
    },
    {
        "title": "Testamentary & Succession",
        "desc":  "Wills, Probate, Letters of Administration, and Succession Certificates with estate planning guidance.",
    },
    {
        "title": "Legal Opinion & Consultation",
        "desc":  "Written legal opinions on regulatory, contractual, and compliance matters.",
    },
    {
        "title": "Contract Review & Vetting",
        "desc":  "Analysing agreements to identify legal risks, unfavourable clauses, and compliance gaps.",
    },
]

COURTS = [
    "Bombay High Court",
    "City Civil & Sessions Court, Mumbai",
    "Commercial Courts, Mumbai",
    "Debt Recovery Tribunal (DRT / DRAT)",
    "National Company Law Tribunal (NCLT / NCLAT)",
    "Consumer Fora — District, State & NCDRC",
    "Labour Courts & Industrial Tribunals",
    "Family Courts, Mumbai & Maharashtra",
    "MahaRERA",
    "GST Appellate & CESTAT",
]

# ── Routes ─────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template(
        "index.html",
        litigation_services=LITIGATION_SERVICES,
        nonlit_services=NONLIT_SERVICES,
        courts=COURTS,
    )


if __name__ == "__main__":
    app.run(debug=True)
