#!/usr/bin/env python3
"""Genera el sitio estático de Venegas Capital Group.

Uso: python3 _build/generate.py  (desde la raíz del repositorio)
Todo el contenido bilingüe vive en este archivo; edítelo aquí y vuelva a generar.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://venegascapitalgroup.com"
HUBSPOT = "https://meetings.hubspot.com/rodrigo578"
LINKEDIN = "https://www.linkedin.com/in/rodvenegas/"
MAIL_U, MAIL_D = "rodrigovenegasmortigo", "gmail.com"
WA = "573155446661"


def t(es, en):
    """Texto en línea bilingüe."""
    if es == en:
        return es
    return f'<span class="es">{es}</span><span class="en">{en}</span>'


def p(es, en, cls=""):
    c = f" {cls}" if cls else ""
    return f'<p class="es{c}">{es}</p><p class="en{c}">{en}</p>'


# ------------------------------------------------------------------ íconos
ICO = {
    "credito": '<path d="M6 34V20M16 34V12M26 34V16M36 34V6"/><path d="M4 34h34" stroke="#A8894B"/>',
    "inversion": '<circle cx="20" cy="20" r="14"/><path d="M20 10v20M15 15h8a3 3 0 010 6h-6a3 3 0 000 6h9" stroke="#A8894B"/>',
    "ma": '<circle cx="14" cy="20" r="9"/><circle cx="26" cy="20" r="9" stroke="#A8894B"/>',
    "activos": '<path d="M6 34V16l14-9 14 9v18z"/><path d="M14 34V24h12v10" stroke="#A8894B"/>',
    "factoring": '<path d="M9 5h16l6 6v24H9z"/><path d="M14 17h12M14 23h12" stroke="#A8894B"/><path d="M14 29h6"/>',
    "cross": '<circle cx="20" cy="20" r="14"/><path d="M6 20h28M20 6c5 4 5 24 0 28M20 6c-5 4-5 24 0 28" stroke="#A8894B"/>',
    "legal": '<path d="M20 5v30M10 35h20"/><path d="M8 13h24" stroke="#A8894B"/><path d="M8 13l-5 11h10zM32 13l-5 11h10z"/>',
    "dd": '<circle cx="17" cy="17" r="10"/><path d="M25 25l10 10" stroke="#A8894B"/><path d="M13 17l3 3 5-6"/>',
    "ai": '<rect x="10" y="10" width="20" height="20"/><path d="M15 4v6M25 4v6M15 30v6M25 30v6M4 15h6M4 25h6M30 15h6M30 25h6" stroke="#A8894B"/><path d="M16 20h8M20 16v8"/>',
    "orig": '<rect x="6" y="10" width="28" height="20"/><path d="M6 16h28" stroke="#A8894B"/><path d="M11 24h8"/>',
    "empresa": '<path d="M6 34V14l10-6v26M16 34V18l18-6v22"/><path d="M4 34h32" stroke="#A8894B"/>',
    "proyecto": '<circle cx="20" cy="14" r="6" stroke="#A8894B"/><path d="M20 4v3M20 21v3M10 14H7M33 14h-3"/><path d="M6 34l6-10h16l6 10z"/>',
    "inversor": '<path d="M8 20h24M24 12l8 8-8 8"/><path d="M8 12v16" stroke="#A8894B"/>',
}


def ico(key, color="#1E4434", cls="ico"):
    return (f'<svg class="{cls}" viewBox="0 0 40 40" fill="none" stroke="{color}" '
            f'stroke-width="2" aria-hidden="true">{ICO[key]}</svg>')


# ------------------------------------------------------------------ servicios
SERVICES = [
    {
        "slug": "credito", "ico": "credito", "hub": ("Crédito", "Credit"),
        "title": ("Crédito corporativo y de proyectos", "Corporate & project credit"),
        "h1": ("Crédito que el comité <em>sí</em> aprueba", "Credit the committee <em>does</em> approve"),
        "short": ("Deuda senior, capital de trabajo, consolidación de pasivos y financiación de proyectos con banca en Colombia y Panamá.",
                  "Senior debt, working capital, liability consolidation and project finance with banks in Colombia and Panama."),
        "lead": ("Preparamos su empresa o su proyecto para pedir crédito con la información, la estructura y las garantías que el banco necesita ver. Identificamos los problemas antes que el analista y negociamos los términos hasta el desembolso.",
                 "We prepare your company or project to request credit with the information, structure and collateral the bank needs to see. We find the issues before the analyst does and negotiate terms through disbursement."),
        "who": ("Empresas con deuda cara o fragmentada, empresas a las que el banco les negó el crédito sin explicar por qué y proyectos con licencias avanzadas que todavía no tienen cierre financiero.",
                "Companies with expensive or fragmented debt, companies turned down by a bank without a clear reason, and projects with permits in place but no financial close yet."),
        "what": [
            ("Diagnóstico de elegibilidad crediticia y capacidad máxima de deuda", "Credit-eligibility diagnosis and maximum debt capacity"),
            ("Consolidación y sustitución de pasivos costosos", "Consolidation and refinancing of expensive liabilities"),
            ("Capital de trabajo, crédito de largo plazo y project finance", "Working capital, long-term loans and project finance"),
            ("Garantías, fiducias y estructuras de fuente de pago", "Collateral, trust vehicles and payment-source structures"),
            ("Presentación y negociación ante banca en Colombia y Panamá", "Placement and negotiation with banks in Colombia and Panama"),
        ],
        "deliv": [
            ("Informe de elegibilidad crediticia con semáforo", "Credit-eligibility report with traffic-light rating"),
            ("Modelo financiero con escenarios de estrés, en Excel", "Financial model with stress scenarios, in Excel"),
            ("Memorando de crédito listo para comité", "Committee-ready credit memorandum"),
            ("Term sheet negociado", "Negotiated term sheet"),
        ],
        "ai": ["diagnostico", "matching", "covenants"],
    },
    {
        "slug": "inversion", "ico": "inversion", "hub": ("Inversión y capital", "Investment & equity"),
        "title": ("Inversión y levantamiento de capital", "Investment & capital raising"),
        "h1": ("Capital para crecer, <em>bien estructurado</em>", "Growth capital, <em>properly structured</em>"),
        "short": ("Equity, deuda privada y mezzanine con fondos, family offices e inversionistas en Estados Unidos, Europa, Reino Unido y Emiratos.",
                  "Equity, private debt and mezzanine with funds, family offices and investors in the U.S., Europe, the U.K. and the UAE."),
        "lead": ("Definimos cuánto capital necesita, de qué tipo y a qué valoración. Preparamos el material de inversión con estándar institucional y lo presentamos a los inversionistas de nuestra red con mayor probabilidad de encaje.",
                 "We define how much capital you need, of what kind and at what valuation. We prepare institutional-grade investment materials and present them to the investors in our network most likely to fit."),
        "who": ("Empresas en expansión, desarrolladores de proyectos de energía e inmobiliarios y originadoras de crédito que necesitan capital más allá de la banca tradicional.",
                "Growing companies, energy and real estate developers and credit originators that need capital beyond traditional banking."),
        "what": [
            ("Mezcla óptima de deuda y capital, y valoración de entrada", "Optimal debt-equity mix and entry valuation"),
            ("Teaser, memorando de inversión y modelo financiero", "Teaser, investment memorandum and financial model"),
            ("Mapeo y acercamiento a inversionistas de nuestra red", "Mapping and outreach to investors in our network"),
            ("Titularización y tokenización de activos cuando aplica", "Securitization and asset tokenization where relevant"),
            ("Gestión del data room, negociación de términos y cierre", "Data room management, term negotiation and closing"),
        ],
        "deliv": [
            ("Teaser y memorando de inversión", "Teaser and investment memorandum"),
            ("Modelo financiero y valoración, en Excel", "Financial model and valuation, in Excel"),
            ("Lista priorizada de inversionistas objetivo", "Prioritized list of target investors"),
            ("Term sheet y documentos de cierre", "Term sheet and closing documents"),
        ],
        "ai": ["dataroom", "matching", "kyc"],
    },
    {
        "slug": "fusiones-adquisiciones", "ico": "ma", "hub": ("M&A", "M&A"),
        "title": ("Fusiones y adquisiciones", "Mergers & acquisitions"),
        "h1": ("Comprar o vender una empresa, <em>sin sorpresas</em>", "Buying or selling a company, <em>without surprises</em>"),
        "short": ("Compra y venta de empresas: valoración, búsqueda de contraparte, due diligence, negociación y documentación.",
                  "Buy-side and sell-side: valuation, counterparty search, due diligence, negotiation and documentation."),
        "lead": ("Acompañamos la transacción completa, desde la valoración hasta la firma. Combinamos el análisis financiero con el criterio legal para que el precio, las garantías y los mecanismos de ajuste queden bien amarrados.",
                 "We support the full transaction, from valuation to signing. We combine financial analysis with legal judgment so that price, warranties and adjustment mechanisms are properly secured."),
        "who": ("Accionistas que quieren vender o dar entrada a un socio, y compradores estratégicos o financieros que buscan adquisiciones en Latinoamérica.",
                "Shareholders who want to sell or bring in a partner, and strategic or financial buyers looking for acquisitions in Latin America."),
        "what": [
            ("Valoración y preparación de la empresa para la venta", "Valuation and sale readiness"),
            ("Búsqueda y filtro de objetivos para compradores", "Target search and screening for buyers"),
            ("Due diligence financiero, legal y de cumplimiento", "Financial, legal and compliance due diligence"),
            ("Estructura de la transacción y financiación de la adquisición", "Deal structure and acquisition financing"),
            ("Negociación del contrato, garantías y ajustes de precio", "Negotiation of the agreement, warranties and price adjustments"),
        ],
        "deliv": [
            ("Informe de valoración", "Valuation report"),
            ("Memorando informativo o lista corta de objetivos", "Information memorandum or target shortlist"),
            ("Informe de due diligence con hallazgos priorizados", "Due diligence report with prioritized findings"),
            ("Documentos de la transacción", "Transaction documents"),
        ],
        "ai": ["dataroom", "kyc", "contratos"],
    },
    {
        "slug": "compraventa-activos", "ico": "activos", "hub": ("Compraventa de activos", "Asset sales"),
        "title": ("Compraventa de activos", "Asset sales & acquisitions"),
        "h1": ("Activos depurados, <em>listos para transar</em>", "Vetted assets, <em>ready to trade</em>"),
        "short": ("Venta y compra de activos de energía, inmobiliarios, logísticos y carteras de crédito, con data room y debida diligencia listos.",
                  "Sale and purchase of energy, real estate and logistics assets and loan books, with data room and due diligence ready."),
        "lead": ("Un activo bien depurado se vende más rápido y a mejor precio. Ordenamos la información legal, técnica y financiera, la presentamos a compradores calificados y estructuramos la venta de la forma más eficiente.",
                 "A well-vetted asset sells faster and at a better price. We organize the legal, technical and financial information, present it to qualified buyers and structure the sale in the most efficient way."),
        "who": ("Propietarios de activos solares, inmobiliarios o logísticos que quieren vender, y fondos, desarrolladores capitalizados e inversionistas que buscan activos verificados.",
                "Owners of solar, real estate or logistics assets who want to sell, and funds, well-capitalized developers and investors looking for verified assets."),
        "what": [
            ("Depuración legal, técnica y financiera del activo", "Legal, technical and financial vetting of the asset"),
            ("Valoración y estrategia de precio", "Valuation and pricing strategy"),
            ("Data room bajo acuerdo de confidencialidad", "Data room under NDA"),
            ("Acceso a compradores estratégicos y fondos", "Access to strategic buyers and funds"),
            ("Estructura de la venta: directa, por vehículo fiduciario o por acciones", "Sale structure: direct, via trust vehicle or share deal"),
        ],
        "deliv": [
            ("Ficha del activo y teaser", "Asset profile and teaser"),
            ("Data room organizado", "Organized data room"),
            ("Informe de debida diligencia", "Due diligence report"),
            ("Contrato de compraventa", "Purchase agreement"),
        ],
        "ai": ["dataroom", "matching", "cartera"],
    },
    {
        "slug": "factoring", "ico": "factoring", "hub": ("Factoring", "Factoring"),
        "title": ("Factoring local e internacional", "Domestic & international factoring"),
        "h1": ("Convierta sus facturas <em>en caja</em>", "Turn your invoices <em>into cash</em>"),
        "short": ("Liquidez sobre cuentas por cobrar en Colombia y en el exterior: factoring, confirming y financiación de exportaciones.",
                  "Liquidity on receivables in Colombia and abroad: factoring, reverse factoring and export finance."),
        "lead": ("Estructuramos la operación de factoring adecuada para su cartera y la gestionamos ante fondos y firmas de factoring aliadas, en Colombia y en el exterior. Para originadoras de factoring, conseguimos el fondeo que su cartera necesita para crecer.",
                 "We structure the right factoring facility for your receivables and arrange it with partner funds and factoring firms in Colombia and abroad. For factoring originators, we secure the funding their book needs to grow."),
        "who": ("Empresas con ventas a crédito que inmovilizan su caja, exportadores con clientes en el exterior y originadoras de factoring que necesitan un segundo fondeador.",
                "Companies whose credit sales tie up their cash, exporters with clients abroad and factoring originators that need a second funder."),
        "what": [
            ("Análisis de la cartera y de la calidad de los pagadores", "Analysis of the receivables and payer quality"),
            ("Modalidad adecuada: con o sin recurso, confirming, factoring de exportación o forfaiting", "The right product: with or without recourse, reverse factoring, export factoring or forfaiting"),
            ("Presentación a fondos y firmas de factoring aliadas", "Placement with partner funds and factoring firms"),
            ("Para originadoras: segundo fondeador, compradores de cartera y titularización", "For originators: second funder, loan-book buyers and securitization"),
            ("Revisión de contratos de cesión y notificación a pagadores", "Review of assignment agreements and payer notices"),
        ],
        "deliv": [
            ("Diagnóstico de cartera y pagadores", "Receivables and payer diagnosis"),
            ("Propuesta de estructura y costo objetivo", "Proposed structure and target cost"),
            ("Contratos revisados y listos para firma", "Reviewed, ready-to-sign agreements"),
        ],
        "ai": ["cartera", "matching", "kyc"],
        "advisory_note": True,
    },
    {
        "slug": "credito-cross-border", "ico": "cross", "hub": ("Crédito cross-border", "Cross-border credit"),
        "title": ("Crédito cross-border", "Cross-border credit"),
        "h1": ("Fondeo internacional para <em>empresas latinoamericanas</em>", "International funding for <em>Latin American companies</em>"),
        "short": ("Fondeo desde Estados Unidos, Europa, Reino Unido y Emiratos para empresas y proyectos latinoamericanos.",
                  "Funding from the U.S., Europe, the U.K. and the UAE for Latin American companies and projects."),
        "lead": ("Cuando la banca local se queda corta, conectamos su empresa o su proyecto con bancos internacionales, fondos de deuda e inversionistas privados. Resolvemos la estructura, las jurisdicciones y el cumplimiento que exige un fondeador extranjero.",
                 "When local banks fall short, we connect your company or project with international banks, debt funds and private investors. We solve the structure, jurisdictions and compliance a foreign lender requires."),
        "who": ("Empresas con ingresos en dólares o exportadoras, y proyectos cuyo tamaño supera el apetito de la banca local.",
                "Companies with dollar revenues or exporters, and projects whose size exceeds local banks' appetite."),
        "what": [
            ("Evaluación de elegibilidad para fondeo internacional", "Eligibility assessment for international funding"),
            ("Deuda privada, préstamos sindicados y financiación de comercio exterior", "Private debt, syndicated loans and trade finance"),
            ("Garantías, cobertura cambiaria y vehículos en Panamá o Estados Unidos", "Collateral, FX hedging and vehicles in Panama or the U.S."),
            ("Cumplimiento cambiario, tributario y KYC/AML", "FX, tax and KYC/AML compliance"),
            ("Gestión ante bancos internacionales, fondos de deuda e inversionistas privados", "Placement with international banks, debt funds and private investors"),
        ],
        "deliv": [
            ("Informe de elegibilidad internacional", "International eligibility report"),
            ("Estructura propuesta con mapa de jurisdicciones", "Proposed structure with jurisdiction map"),
            ("Paquete KYC y de cumplimiento", "KYC and compliance package"),
            ("Term sheet negociado", "Negotiated term sheet"),
        ],
        "ai": ["diagnostico", "kyc", "contratos"],
        "advisory_note": True,
    },
]

LEGAL = {
    "slug": "acompanamiento-legal", "ico": "legal",
    "title": ("Acompañamiento legal transversal", "End-to-end legal support"),
    "h1": ("El abogado que <em>entiende la operación</em>", "The lawyer who <em>understands the deal</em>"),
    "short": ("Asesoría y acompañamiento legal en todas las transacciones, desde el term sheet hasta el cierre, en español e inglés.",
              "Legal advice and support across every transaction, from term sheet to closing, in Spanish and English."),
    "lead": ("Cada transacción que estructuramos lleva acompañamiento legal de principio a fin. Un mismo equipo diseña la estructura financiera y redacta los documentos, así nada se pierde entre el banquero y el abogado.",
             "Every transaction we structure comes with legal support from start to finish. The same team designs the financial structure and drafts the documents, so nothing gets lost between the banker and the lawyer."),
    "who": ("Todos los clientes de la firma, y empresas que ya tienen fondeador o comprador y necesitan un abogado con criterio financiero para cerrar.",
            "Every client of the firm, and companies that already have a funder or buyer and need a lawyer with financial judgment to close."),
    "what": [
        ("Term sheets, cartas de intención y acuerdos de confidencialidad", "Term sheets, letters of intent and NDAs"),
        ("Contratos de crédito, garantías, fiducias y cesión de cartera", "Loan agreements, collateral, trusts and receivables assignment"),
        ("Contratos de compraventa de acciones y de activos", "Share and asset purchase agreements"),
        ("Contratos bilingües cuando la contraparte es internacional", "Bilingual agreements with international counterparties"),
        ("Cumplimiento fintech, protección de datos y prevención de lavado de activos", "Fintech compliance, data protection and anti-money laundering"),
    ],
    "deliv": [
        ("Documentos de la transacción", "Transaction documents"),
        ("Matriz de riesgos legales", "Legal risk matrix"),
        ("Lista de condiciones precedentes para el cierre", "Conditions-precedent checklist for closing"),
    ],
    "ai": ["contratos", "kyc", "gobierno"],
}

ALL_SERVICES = SERVICES + [LEGAL]

# ------------------------------------------------------------------ IA
AI = {
    "diagnostico": {
        "group": ("Diagnóstico", "Diagnosis"),
        "title": ("Diagnóstico de bancabilidad exprés", "Express bankability diagnosis"),
        "desc": ("En 48 a 72 horas, a partir de estados financieros, extractos y certificados: semáforo de elegibilidad, capacidad máxima de deuda y brechas a cerrar antes de ir al banco.",
                 "In 48 to 72 hours, from financial statements, bank statements and certificates: eligibility rating, maximum debt capacity and gaps to close before approaching the bank."),
        "items": [("Semáforo Cumple · Vigilar · Alerta", "Pass · Watch · Alert rating"),
                  ("Capacidad máxima de deuda", "Maximum debt capacity"),
                  ("Plan de acción priorizado", "Prioritized action plan")],
    },
    "dataroom": {
        "group": ("Diagnóstico", "Diagnosis"),
        "title": ("Data room inteligente", "Intelligent data room"),
        "desc": ("Clasificamos e indexamos la documentación, detectamos faltantes y banderas rojas, y habilitamos consultas en lenguaje natural para el inversionista.",
                 "We classify and index the documentation, flag gaps and red flags, and enable natural-language questions for investors."),
        "items": [("Índice y lista de faltantes", "Index and gap list"),
                  ("Banderas rojas por severidad", "Red flags by severity"),
                  ("Preguntas y respuestas sobre los documentos", "Q&A over the documents")],
    },
    "matching": {
        "group": ("Colocación", "Placement"),
        "title": ("Matching de fondeadores", "Funder matching"),
        "desc": ("Cruzamos el perfil de la operación con el apetito de bancos, fondos y compradores de cartera de nuestra red para priorizar a quién presentarla.",
                 "We match the deal profile against the appetite of banks, funds and loan-book buyers in our network to prioritize who to approach."),
        "items": [("Lista corta de fondeadores", "Funder shortlist"),
                  ("Encaje por ticket, sector y garantías", "Fit by ticket, sector and collateral"),
                  ("Orden de acercamiento recomendado", "Recommended outreach sequence")],
    },
    "cartera": {
        "group": ("Colocación", "Placement"),
        "title": ("Analítica de cartera", "Loan-book analytics"),
        "desc": ("Cosechas, mora por tramo, concentración por pagador y escenarios de estrés, en el formato que pide un comprador de cartera o una titularización.",
                 "Vintages, delinquency buckets, payer concentration and stress scenarios, in the format a loan-book buyer or securitization requires."),
        "items": [("Análisis de cosechas y mora", "Vintage and delinquency analysis"),
                  ("Concentración y calidad de pagadores", "Payer concentration and quality"),
                  ("Cinta de datos lista para el comprador", "Buyer-ready data tape")],
    },
    "covenants": {
        "group": ("Seguimiento", "Monitoring"),
        "title": ("Monitoreo de covenants", "Covenant monitoring"),
        "desc": ("Después del cierre, un tablero mensual con semáforo de covenants y alertas tempranas para el cliente y el fondeador.",
                 "After closing, a monthly dashboard with covenant ratings and early warnings for the client and the lender."),
        "items": [("Tablero mensual", "Monthly dashboard"),
                  ("Alertas tempranas de incumplimiento", "Early breach warnings"),
                  ("Reporte para el fondeador", "Lender reporting")],
    },
    "kyc": {
        "group": ("Seguimiento", "Monitoring"),
        "title": ("Due diligence de contrapartes (KYC/AML)", "Counterparty due diligence (KYC/AML)"),
        "desc": ("Listas restrictivas, medios adversos y beneficiario final de compradores, vendedores y fondeadores, con un informe trazable.",
                 "Sanctions lists, adverse media and beneficial ownership of buyers, sellers and funders, with a traceable report."),
        "items": [("Listas restrictivas y PEP", "Sanctions and PEP screening"),
                  ("Medios adversos", "Adverse media"),
                  ("Beneficiario final", "Beneficial ownership")],
    },
    "contratos": {
        "group": ("Legal", "Legal"),
        "title": ("Revisión contractual bilingüe", "Bilingual contract review"),
        "desc": ("Marcamos riesgos, cláusulas fuera de mercado y diferencias entre las versiones en español e inglés de cada contrato.",
                 "We flag risks, off-market clauses and discrepancies between the Spanish and English versions of each agreement."),
        "items": [("Matriz de riesgos por cláusula", "Clause-by-clause risk matrix"),
                  ("Comparación de versiones ES/EN", "ES/EN version comparison"),
                  ("Propuesta de redacción", "Proposed wording")],
    },
    "gobierno": {
        "group": ("Legal", "Legal"),
        "title": ("Gobierno de IA para entidades financieras", "AI governance for financial firms"),
        "desc": ("Políticas de uso de IA, matriz de riesgos y controles para fintech, originadoras y fondos que ya usan IA en crédito o cumplimiento.",
                 "AI use policies, risk matrix and controls for fintechs, originators and funds already using AI in credit or compliance."),
        "items": [("Política de uso de IA", "AI use policy"),
                  ("Matriz de riesgos y controles", "Risk and control matrix"),
                  ("Capacitación del equipo", "Team training")],
    },
}
AI_ORDER = ["diagnostico", "dataroom", "matching", "cartera", "covenants", "kyc", "contratos", "gobierno"]

# ------------------------------------------------------------------ piezas comunes
DISCLAIMER = t(
    "Venegas Capital Group es la marca de la práctica de asesoría profesional independiente de Rodrigo Venegas. No es una entidad financiera: no capta recursos del público, no otorga crédito, no compra facturas ni cartera y no realiza intermediación de valores. Estructuramos las operaciones y las gestionamos ante bancos, fondos y fondeadores aliados, que toman sus propias decisiones de crédito e inversión. Nada en este sitio constituye una oferta de valores.",
    "Venegas Capital Group is the brand of Rodrigo Venegas's independent professional advisory practice. It is not a financial institution: it does not take deposits, lend, purchase invoices or loan books, or act as a broker-dealer. We structure transactions and arrange them with partner banks, funds and lenders, who make their own credit and investment decisions. Nothing on this site is an offer of securities.")

ADVISORY_NOTE = t(
    "Nuestro rol es de estructurador y gestor: preparamos la operación y la presentamos a fondeadores aliados. No otorgamos financiación ni compramos facturas o cartera.",
    "Our role is that of arranger and advisor: we prepare the transaction and present it to partner funders. We do not lend or purchase invoices or loan books.")

MAIL_SVG = '<svg viewBox="0 0 24 24" width="44" height="44" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><rect x="3" y="5" width="18" height="14"/><path d="M3 6l9 7 9-7"/></svg>'
WA_SVG = '<svg viewBox="0 0 24 24" width="44" height="44" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round" aria-hidden="true"><path d="M12 3a9 9 0 00-7.8 13.5L3 21l4.6-1.2A9 9 0 1012 3z"/><path d="M8.6 7.8c.3-.3.8-.3 1 .1l.8 1.7c.1.3 0 .6-.2.8l-.5.5c.6 1.3 1.6 2.3 2.9 2.9l.5-.5c.2-.2.5-.3.8-.2l1.7.8c.4.2.4.7.1 1-.9.9-2.2 1.1-3.3.5a9.4 9.4 0 01-4.3-4.3c-.6-1.1-.4-2.4.5-3.3z" fill="currentColor" stroke="none"/></svg>'
LI_PATH = '<path d="M4.98 3.5a2.5 2.5 0 11-.02 5 2.5 2.5 0 01.02-5zM3 9h4v12H3zM9 9h3.8v1.7h.05c.53-1 1.83-2.05 3.77-2.05C20.6 8.65 21 11.2 21 14.5V21h-4v-5.8c0-1.4-.03-3.2-1.95-3.2-1.95 0-2.25 1.5-2.25 3.1V21H9z"/>'
LI_SVG = f'<svg viewBox="0 0 24 24" width="44" height="44" fill="currentColor" aria-hidden="true">{LI_PATH}</svg>'
CAL_SVG = '<svg viewBox="0 0 24 24" width="44" height="44" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><rect x="3" y="5" width="18" height="16"/><path d="M3 10h18M8 3v4M16 3v4"/><path d="M8 14h2M11 14h2M14 14h2M8 17h2M11 17h2" stroke-width="1.8"/></svg>'

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
           "%3Crect width='64' height='64' fill='%23143026'/%3E%3Ctext x='32' y='41' font-family='Georgia,serif' "
           "font-size='22' font-weight='bold' fill='%23A8894B' text-anchor='middle'%3EVCG%3C/text%3E%3C/svg%3E")

HERO_BG = '''<svg class="bg" viewBox="0 0 1200 700" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
  <defs>
    <linearGradient id="g1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0E231B"/><stop offset="1" stop-color="#1E4434"/></linearGradient>
    <radialGradient id="glow" cx="78%" cy="42%" r="48%"><stop offset="0" stop-color="#33705A" stop-opacity=".55"/><stop offset="1" stop-color="#143026" stop-opacity="0"/></radialGradient>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#33705A" stroke-opacity=".16" stroke-width="1"/></pattern>
  </defs>
  <rect width="1200" height="700" fill="url(#g1)"/><rect width="1200" height="700" fill="url(#grid)"/><rect width="1200" height="700" fill="url(#glow)"/>
  <g fill="none" stroke="#A8894B" stroke-opacity=".5">
    <circle cx="940" cy="300" r="140"/><circle cx="940" cy="300" r="215" stroke-opacity=".25"/><circle cx="940" cy="300" r="300" stroke-opacity=".12"/>
    <ellipse cx="940" cy="300" rx="300" ry="90" stroke-opacity=".3" transform="rotate(-18 940 300)"/>
  </g>
  <g stroke="#9CC7B2" stroke-opacity=".4"><line x1="940" y1="300" x2="940" y2="160"/><line x1="940" y1="300" x2="1061" y2="230"/><line x1="940" y1="300" x2="1061" y2="370"/><line x1="940" y1="300" x2="940" y2="440"/><line x1="940" y1="300" x2="819" y2="370"/><line x1="940" y1="300" x2="819" y2="230"/></g>
  <g fill="#A8894B"><circle cx="940" cy="300" r="7"/><circle cx="940" cy="160" r="4"/><circle cx="1061" cy="230" r="4"/><circle cx="1061" cy="370" r="4"/><circle cx="940" cy="440" r="4"/><circle cx="819" cy="370" r="4"/><circle cx="819" cy="230" r="4"/></g>
</svg>'''


def nav(current):
    sub = "".join(f'<li><a href="/servicios/{s["slug"]}/">{t(*s["title"])}</a></li>' for s in ALL_SERVICES)

    def cur(key):
        return ' aria-current="page"' if key == current else ""
    return f'''<a class="skip" href="#main">{t("Ir al contenido", "Skip to content")}</a>
<header class="nav">
  <div class="wrap">
    <a class="brand" href="/" aria-label="Venegas Capital Group"><span class="mono">VCG</span><span class="name">VENEGAS<small>CAPITAL GROUP</small></span></a>
    <ul class="menu">
      <li class="has-sub"><a href="/servicios/"{cur("servicios")}>{t("Servicios", "Services")}</a><ul class="sub">{sub}</ul></li>
      <li><a href="/inteligencia-artificial/"{cur("ia")}>{t("IA aplicada", "Applied AI")}</a></li>
      <li><a href="/firma/"{cur("firma")}>{t("La firma", "The firm")}</a></li>
      <li><a href="/contacto/"{cur("contacto")}>{t("Contacto", "Contact")}</a></li>
    </ul>
    <div class="right">
      <a class="nav-cta" href="{HUBSPOT}" target="_blank" rel="noopener">{t("Agendar", "Book a call")}</a>
      <div class="lang" role="group" aria-label="Idioma / Language"><button type="button" data-set="es" aria-pressed="true">ES</button><button type="button" data-set="en" aria-pressed="false">EN</button></div>
      <button class="burger" type="button" aria-label="Menú" aria-expanded="false"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 6h18M3 12h18M3 18h18"/></svg></button>
    </div>
  </div>
</header>'''


def contact_tiles():
    return f'''<div class="contact-grid">
      <a class="js-mail" href="/contacto/" data-u="{MAIL_U}" data-d="{MAIL_D}" aria-label="Email"><small>Email</small><span class="ci">{MAIL_SVG}</span><em>{t("Escríbanos", "Write to us")}</em></a>
      <a class="js-wa" href="/contacto/" data-n="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp"><small>WhatsApp</small><span class="ci">{WA_SVG}</span><em>{t("Enviar mensaje", "Send a message")}</em></a>
      <a href="{LINKEDIN}" target="_blank" rel="noopener" aria-label="LinkedIn"><small>LinkedIn</small><span class="ci">{LI_SVG}</span><em>{t("Perfil del socio director", "Managing partner's profile")}</em></a>
      <a href="{HUBSPOT}" target="_blank" rel="noopener"><small>{t("Agendar llamada", "Book a call")}</small><span class="ci">{CAL_SVG}</span><em>{t("Reservar 30 minutos", "Book 30 minutes")}</em></a>
    </div>'''


def contact_band(num=None):
    n = f'<div class="band"><span class="num">{num}</span><span class="rule"></span></div>' if num else '<div class="band"><span class="rule"></span></div>'
    return f'''<section class="block contact">
  <div class="wrap">
    {n}
    <h2>{t("Conversemos sobre su operación", "Let's talk about your transaction")}</h2>
    {p("Una primera llamada de 30 minutos basta para saber si su operación está lista para presentarse a un fondeador y qué le falta.", "A first 30-minute call is enough to know whether your transaction is ready to go to a funder and what it still needs.", "intro")}
    {contact_tiles()}
  </div>
</section>'''


def footer():
    svc = "".join(f'<li><a href="/servicios/{s["slug"]}/">{t(*s["title"])}</a></li>' for s in ALL_SERVICES)
    return f'''<footer class="foot">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <b>VENEGAS CAPITAL GROUP</b>
        <p style="margin-top:10px;color:#C6D6CD">{t("Estructuración financiera, banca de inversión y derecho financiero para Latinoamérica, Estados Unidos y Europa.", "Financial structuring, investment banking and financial law for Latin America, the United States and Europe.")}</p>
        <p style="margin-top:12px;letter-spacing:.14em;text-transform:uppercase;font-size:13px;color:var(--menta)">Bogotá · Panamá · Miami</p>
      </div>
      <div><h4>{t("Servicios", "Services")}</h4><ul>{svc}</ul></div>
      <div><h4>{t("La firma", "The firm")}</h4><ul>
        <li><a href="/inteligencia-artificial/">{t("IA aplicada", "Applied AI")}</a></li>
        <li><a href="/firma/">{t("Socio director y trayectoria", "Managing partner & track record")}</a></li>
        <li><a href="/contacto/">{t("Contacto", "Contact")}</a></li>
        <li><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a></li>
      </ul></div>
    </div>
    <p class="disc">© <span class="yr">2026</span> Venegas Capital Group. {DISCLAIMER}</p>
  </div>
</footer>'''


def page(path, key, title_es, title_en, desc_es, body, schema=None):
    canonical = DOMAIN + path
    ld = f'<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>' if schema else ""
    html = f'''<!DOCTYPE html>
<html lang="es" data-lang="es" data-title-es="{title_es}" data-title-en="{title_en}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title_es}</title>
<meta name="description" content="{desc_es}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title_es}">
<meta property="og:description" content="{desc_es}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{DOMAIN}/assets/og.png">
<meta property="og:locale" content="es_CO">
<meta property="og:locale:alternate" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#143026">
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Carlito:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/styles.css">
{ld}
</head>
<body>
{nav(key)}
<main id="main">
{body}
</main>
{footer()}
<script src="/assets/site.js"></script>
</body>
</html>
'''
    out = os.path.join(ROOT, path.strip("/"), "index.html") if path != "/" else os.path.join(ROOT, "index.html")
    if path.endswith(".html"):
        out = os.path.join(ROOT, path.strip("/"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    return path


def hero(kicker, h1, lead, ctas=True, page_cls="", crumbs=""):
    cta = ""
    if ctas:
        cta = f'''<div class="cta">
      <a class="btn primary" href="{HUBSPOT}" target="_blank" rel="noopener">{t("Agendar una conversación", "Book a conversation")}</a>
      <a class="btn ghost" href="/servicios/">{t("Ver servicios", "View services")}</a>
    </div>'''
    return f'''<section class="hero{page_cls}">
  {HERO_BG}
  <div class="wrap">
    {crumbs}
    <div class="kicker">{kicker}</div>
    <h1>{h1}</h1>
    <div class="filete"></div>
    {lead}
    {cta}
    <div class="loc">Bogotá · Panamá · Miami</div>
  </div>
</section>'''


def section(num, h2, inner, cls="", intro=None, sid=""):
    i = p(*intro, "intro") if intro else ""
    idattr = f' id="{sid}"' if sid else ""
    return f'''<section class="block {cls}"{idattr}>
  <div class="wrap">
    <div class="band"><span class="num">{num}</span><span class="rule"></span></div>
    <h2>{h2}</h2>
    {i}
    {inner}
  </div>
</section>'''


def service_cards():
    cards = "".join(
        f'<a class="card" href="/servicios/{s["slug"]}/">{ico(s["ico"])}<h3>{t(*s["title"])}</h3><p>{t(*s["short"])}</p><span class="more">{t("Ver servicio →", "View service →")}</span></a>'
        for s in SERVICES)
    cards += (f'<a class="card legal" href="/servicios/{LEGAL["slug"]}/">{ico("legal", "#A8894B")}<div><h3>{t(*LEGAL["title"])}</h3>'
              f'<p>{t("Por debajo de las seis líneas: el mismo equipo que diseña la estructura financiera redacta y negocia los documentos, desde el term sheet hasta el cierre, en español e inglés.", "Underpinning all six lines: the same team that designs the financial structure drafts and negotiates the documents, from term sheet to closing, in Spanish and English.")}</p>'
              f'<span class="more" style="color:var(--oro)">{t("Ver servicio →", "View service →")}</span></div></a>')
    return f'<div class="grid">{cards}</div>'


def hub_svg():
    cx, cy, r = 360, 225, 180
    import math
    nodes = []
    for i, s in enumerate(SERVICES):
        ang = math.radians(-90 + 60 * i)
        nodes.append((cx + r * math.cos(ang), cy + r * math.sin(ang), s))
    lines = "".join(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}"/>' for x, y, _ in nodes)
    labels = ""
    for x, y, s in nodes:
        w = 196
        es, en = s["hub"]
        labels += (f'<a href="/servicios/{s["slug"]}/"><rect class="lbl" x="{x - w/2:.0f}" y="{y - 22:.0f}" width="{w}" height="44" fill="#fff" stroke="#A8894B"/>'
                   f'<text class="lt es" x="{x:.0f}" y="{y + 6:.0f}" text-anchor="middle" font-family="Georgia,serif" font-size="17" fill="#1E4434">{es}</text>'
                   f'<text class="lt en" x="{x:.0f}" y="{y + 6:.0f}" text-anchor="middle" font-family="Georgia,serif" font-size="17" fill="#1E4434">{en}</text></a>')
    return f'''<div class="hub"><svg viewBox="0 0 720 520" role="img" aria-label="Estructuración al centro de siete líneas de servicio / Structuring at the center of seven service lines">
  <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#D9E2DC" stroke-dasharray="4 6"/>
  <g stroke="#33705A" stroke-width="1.5">{lines}</g>
  <circle cx="{cx}" cy="{cy}" r="86" fill="#143026" stroke="#A8894B" stroke-width="2"/>
  <circle cx="{cx}" cy="{cy}" r="98" fill="none" stroke="#A8894B" stroke-opacity=".4"/>
  <text class="es" x="{cx}" y="{cy - 4}" text-anchor="middle" font-family="Georgia,serif" font-size="17" font-weight="bold" fill="#fff" letter-spacing="1.5">ESTRUCTURACIÓN</text>
  <text class="en" x="{cx}" y="{cy - 4}" text-anchor="middle" font-family="Georgia,serif" font-size="17" font-weight="bold" fill="#fff" letter-spacing="1.5">STRUCTURING</text>
  <text class="es" x="{cx}" y="{cy + 20}" text-anchor="middle" font-family="Calibri,Carlito,Arial,sans-serif" font-size="13" fill="#C9AE74" letter-spacing="2">PUERTA DE ENTRADA</text>
  <text class="en" x="{cx}" y="{cy + 20}" text-anchor="middle" font-family="Calibri,Carlito,Arial,sans-serif" font-size="13" fill="#C9AE74" letter-spacing="2">POINT OF ENTRY</text>
  {labels}
  <a href="/servicios/{LEGAL["slug"]}/"><rect class="lbl" x="40" y="452" width="640" height="52" fill="#143026"/>
  <text class="lt es" x="360" y="484" text-anchor="middle" font-family="Georgia,serif" font-size="17" fill="#fff">Acompañamiento legal en todas las transacciones</text>
  <text class="lt en" x="360" y="484" text-anchor="middle" font-family="Georgia,serif" font-size="17" fill="#fff">Legal support across every transaction</text></a>
</svg></div>'''


def ai_cards(keys, light=False):
    out = ""
    for k in keys:
        a = AI[k]
        items = "".join(f"<li>{t(*i)}</li>" for i in a["items"])
        out += f'<div class="ai"><div class="tag">{t(*a["group"])}</div><h3>{t(*a["title"])}</h3><p>{t(*a["desc"])}</p><ul>{items}</ul></div>'
    cls = "ai-grid ai-light" if light else "ai-grid"
    return f'<div class="{cls}">{out}</div>'


STEPS = [
    (("FASE 1", "PHASE 1"), ("Diagnóstico", "Diagnosis"), ("Lectura de estados financieros, estructura societaria y necesidad real de financiación.", "Review of financial statements, corporate structure and actual funding need.")),
    (("FASE 2", "PHASE 2"), ("Due diligence", "Due diligence"), ("Hallazgos priorizados por severidad y plan de acción para cerrar brechas antes de ir al mercado.", "Findings ranked by severity and an action plan to close gaps before going to market.")),
    (("FASE 3", "PHASE 3"), ("Estructuración", "Structuring"), ("Estructura, escenarios de estrés, documentos legales y material para inversionistas de estándar institucional.", "Structure, stress scenarios, legal documents and institutional-grade investor materials.")),
    (("FASE 4", "PHASE 4"), ("Colocación y cierre", "Placement & closing"), ("Presentación a fondeadores o compradores, negociación de términos y acompañamiento hasta el desembolso.", "Introduction to funders or buyers, term negotiation and support through disbursement.")),
]


def steps():
    return '<div class="steps">' + "".join(
        f'<div class="step"><div class="n">{t(*n)}</div><h3>{t(*h)}</h3><p>{t(*d)}</p></div>' for n, h, d in STEPS) + "</div>"


STATS = '''<section class="stats" aria-label="Cifras">
  <div class="wrap">
    <div class="stat"><b>18+</b>''' + t("años en banca y estructuración", "years in banking & structuring") + '''</div>
    <div class="stat"><b>USD 300M+</b>''' + t("en transacciones estructuradas", "in structured transactions") + '''</div>
    <div class="stat"><b>5</b>''' + t("mercados de fondeo: CO · PA · EE. UU. · UK · EAU", "funding markets: CO · PA · U.S. · UK · UAE") + '''</div>
    <div class="stat"><b>10+</b>''' + t("empresas fundadas · 2 exits", "companies founded · 2 exits") + '''</div>
  </div>
</section>'''


# ------------------------------------------------------------------ páginas
def build_home():
    clients = [
        ("orig", ("Originadoras de crédito", "Credit originators"), ("Fintech, factoring y libranza cuya cartera crece más rápido que su fondeo: segundo fondeador, compradores de cartera y titularización.", "Fintech, factoring and payroll lenders whose book grows faster than their funding: second funder, loan-book buyers and securitization.")),
        ("empresa", ("Empresas medianas", "Mid-sized companies"), ("Empresas con deuda cara o fragmentada, que necesitan liquidez o a las que el banco les dice que no sin explicar por qué.", "Companies with expensive or fragmented debt, in need of liquidity, or turned down by banks without a clear reason.")),
        ("proyecto", ("Desarrolladores de proyectos", "Project developers"), ("Proyectos de energía e inmobiliarios con licencias avanzadas y sin cierre financiero, en Colombia y la región.", "Energy and real estate projects with permits in place and no financial close, in Colombia and the region.")),
        ("inversor", ("Compradores e inversionistas", "Buyers & investors"), ("Fondos, family offices y compradores estratégicos que buscan empresas y activos depurados, con data room listo.", "Funds, family offices and strategic buyers looking for vetted companies and assets, with data room ready.")),
    ]
    ccards = "".join(f'<div class="card">{ico(i)}<h3>{t(*h)}</h3><p>{t(*d)}</p></div>' for i, h, d in clients)
    body = hero(
        t("Banca de inversión · Estructuración · Derecho financiero", "Investment banking · Structuring · Financial law"),
        t("Toda gran transacción <em>empieza por estructurar</em>", "Every great transaction <em>starts with structure</em>"),
        p("Venegas Capital Group estructura crédito, inversión, fusiones y adquisiciones, compraventa de activos, factoring y fondeo cross-border para empresas y proyectos en Latinoamérica, Estados Unidos y Europa, con acompañamiento legal en cada operación.",
          "Venegas Capital Group structures credit, investment, M&A, asset sales, factoring and cross-border funding for companies and projects across Latin America, the United States and Europe, with legal support on every transaction.", "lead"))
    body += STATS
    body += section("01", t("Una sola puerta de entrada para siete tipos de transacción", "One point of entry for seven types of transaction"),
                    hub_svg() + service_cards(), sid="servicios",
                    intro=("Antes de hablar con un banco, un fondo o un comprador, la operación tiene que estar estructurada: información ordenada, riesgos identificados y una estructura que el fondeador pueda aprobar. Desde ahí acompañamos cualquiera de estas transacciones hasta el cierre.",
                           "Before talking to a bank, a fund or a buyer, the transaction has to be structured: organized information, identified risks and a structure the funder can approve. From there we carry any of these transactions through to closing."))
    body += section("02", t("Trabajamos con cuatro tipos de cliente que necesitan capital o liquidez", "We work with four types of clients that need capital or liquidity"),
                    f'<div class="grid g4">{ccards}</div>', cls="alt")
    body += section("03", t("Un proceso en cuatro fases que reduce el riesgo de rechazo", "A four-phase process that reduces the risk of rejection"), steps())
    body += section("04", t("Inteligencia artificial aplicada a cada fase de la estructuración", "Artificial intelligence applied to every phase of structuring"),
                    ai_cards(["diagnostico", "matching", "covenants", "contratos"]) +
                    f'<div class="cta"><a class="btn primary" href="/inteligencia-artificial/">{t("Ver los ocho servicios con IA", "See all eight AI services")}</a></div>',
                    cls="dark",
                    intro=("Usamos IA para hacer en días lo que antes tomaba semanas: leer estados financieros, organizar data rooms, cruzar operaciones con fondeadores y vigilar covenants. El criterio y la firma siguen siendo de un profesional con 18 años de experiencia.",
                           "We use AI to do in days what used to take weeks: reading financial statements, organizing data rooms, matching deals with funders and monitoring covenants. The judgment and the sign-off remain with a professional with 18 years of experience."))
    firm = f'''<div class="about">
      <div>
        {p("Venegas Capital Group está liderada por Rodrigo Venegas, abogado y banquero de inversión con más de 18 años en banca privada, estructuración financiera, fusiones y adquisiciones y levantamiento de capital en Latinoamérica, Estados Unidos y Europa.", "Venegas Capital Group is led by Rodrigo Venegas, a lawyer and investment banker with more than 18 years in private banking, financial structuring, M&A and capital raising across Latin America, the United States and Europe.")}
        {p("La firma reúne en un mismo equipo el análisis financiero y el criterio legal. El resultado son operaciones que llegan al comité con los riesgos resueltos y documentos que reflejan exactamente lo que se negoció.", "The firm brings financial analysis and legal judgment together in one team. The result is transactions that reach the committee with risks resolved and documents that reflect exactly what was negotiated.")}
        <div class="cta" style="margin-top:28px"><a class="btn dark" href="/firma/">{t("Conocer la firma y la trayectoria", "Meet the firm and its track record")}</a></div>
      </div>
      <aside class="callout">
        <h3>{t("Socio director", "Managing partner")}</h3>
        <ul>
          <li><b>Rodrigo Venegas</b></li>
          <li>{t("Abogado, Universidad de La Sabana", "Law degree (LL.B.), Universidad de La Sabana")}</li>
          <li>EMBA — Quantic School of Business and Technology, Washington D.C.</li>
          <li>{t("Certificaciones en blockchain y en desarrollo y gobierno de IA", "Certifications in blockchain and in AI development & governance")}</li>
          <li>{t("Español nativo · Inglés C2", "Native Spanish · C2 English")}</li>
        </ul>
      </aside>
    </div>'''
    body += section("05", t("Una firma que integra la banca de inversión y el derecho financiero", "A firm that integrates investment banking and financial law"), firm, cls="alt")
    body += contact_band("06")
    schema = {
        "@context": "https://schema.org", "@type": "ProfessionalService", "name": "Venegas Capital Group",
        "url": DOMAIN + "/", "description": "Estructuración financiera, crédito, inversión, M&A, compraventa de activos, factoring y crédito cross-border con acompañamiento legal.",
        "areaServed": ["Colombia", "Panamá", "Estados Unidos", "Latinoamérica", "Europa"],
        "address": {"@type": "PostalAddress", "addressLocality": "Bogotá", "addressCountry": "CO"},
        "founder": {"@type": "Person", "name": "Rodrigo Venegas", "jobTitle": "Socio director", "sameAs": [LINKEDIN]},
        "sameAs": [LINKEDIN], "knowsLanguage": ["es", "en"],
    }
    page("/", "inicio", "Venegas Capital Group · Estructuración financiera", "Venegas Capital Group · Financial structuring",
         "Venegas Capital Group: estructuración de crédito, inversión, M&A, compraventa de activos, factoring y crédito cross-border con acompañamiento legal. Bogotá · Panamá · Miami.",
         body, schema)


def build_services_index():
    body = hero(t("Servicios", "Services"),
                t("Siete líneas de servicio, <em>una misma puerta de entrada</em>", "Seven service lines, <em>one point of entry</em>"),
                p("Toda operación empieza por un diagnóstico y una estructura. Desde ahí la llevamos al mercado que corresponde: banca, fondos, compradores o fondeadores internacionales.",
                  "Every transaction starts with a diagnosis and a structure. From there we take it to the right market: banks, funds, buyers or international lenders.", "lead"),
                page_cls=" page")
    body += section("01", t("Del diagnóstico al cierre, en cualquiera de estas transacciones", "From diagnosis to closing, in any of these transactions"), hub_svg() + service_cards())
    body += section("02", t("El mismo proceso en cuatro fases para todas", "The same four-phase process for all of them"), steps(), cls="alt")
    body += contact_band()
    page("/servicios/", "servicios", "Servicios · Venegas Capital Group", "Services · Venegas Capital Group",
         "Crédito, inversión, M&A, compraventa de activos, factoring local e internacional, crédito cross-border y acompañamiento legal.", body)


def build_service(s):
    what = "".join(f"<li>{t(*w)}</li>" for w in s["what"])
    deliv = "".join(f"<li>{t(*d)}</li>" for d in s["deliv"])
    crumbs = f'<div class="crumbs"><a href="/servicios/">{t("Servicios", "Services")}</a> /</div>'
    body = hero(t(*s["title"]), t(*s["h1"]), p(*s["lead"], "lead"), page_cls=" page", crumbs=crumbs)
    note = f'<p class="note">{ADVISORY_NOTE}</p>' if s.get("advisory_note") else ""
    legal_link = "" if s["slug"] == LEGAL["slug"] else (
        f'<div class="panel gold"><h3>{t("Con acompañamiento legal", "With legal support")}</h3>'
        f'<p style="font-size:16.5px">{t("Redactamos y negociamos todos los documentos de la operación, en español e inglés.", "We draft and negotiate every transaction document, in Spanish and English.")} '
        f'<a href="/servicios/{LEGAL["slug"]}/">{t("Ver acompañamiento legal →", "See legal support →")}</a></p></div>')
    two = f'''<div class="two">
      <div>
        <ul class="checks">{what}</ul>
        {note}
      </div>
      <div>
        <div class="panel"><h3>{t("Para quién", "Who it's for")}</h3><p style="font-size:16.5px">{t(*s["who"])}</p></div>
        <div class="panel"><h3>{t("Entregables", "Deliverables")}</h3><ul>{deliv}</ul></div>
        {legal_link}
      </div>
    </div>'''
    body += section("01", t("Qué hacemos", "What we do"), two)
    body += section("02", t("Inteligencia artificial que acelera este servicio", "Artificial intelligence that speeds up this service"),
                    ai_cards(s["ai"]) + f'<div class="cta"><a class="btn primary" href="/inteligencia-artificial/">{t("Ver todos los servicios con IA", "See all AI services")}</a></div>',
                    cls="dark")
    others = "".join(f'<a href="/servicios/{o["slug"]}/">{t(*o["title"])}</a>' for o in ALL_SERVICES if o["slug"] != s["slug"])
    body += section("03", t("Cómo trabajamos", "How we work"), steps() + f'<h3 style="margin-top:56px;font-size:20px">{t("Otras líneas de servicio", "Other service lines")}</h3><div class="related">{others}</div>', cls="alt")
    body += contact_band()
    te, tn = s["title"]
    page(f'/servicios/{s["slug"]}/', "servicios", f"{te} · Venegas Capital Group", f"{tn} · Venegas Capital Group", s["short"][0], body)


def build_ai():
    body = hero(t("IA aplicada a la estructuración", "AI applied to structuring"),
                t("Inteligencia artificial, <em>criterio humano</em>", "Artificial intelligence, <em>human judgment</em>"),
                p("Ocho servicios que usan IA para acortar los tiempos del diagnóstico, la colocación y el seguimiento de una operación. Cada entregable lo revisa y lo firma un profesional.",
                  "Eight services that use AI to shorten the time needed for diagnosis, placement and monitoring of a transaction. A professional reviews and signs off every deliverable.", "lead"),
                page_cls=" page")
    groups = [
        ("01", ("Diagnóstico: saber en días si su operación es financiable", "Diagnosis: know in days whether your deal is financeable"), ["diagnostico", "dataroom"], ""),
        ("02", ("Colocación: llegar al fondeador correcto con la información correcta", "Placement: reach the right funder with the right information"), ["matching", "cartera"], "alt"),
        ("03", ("Seguimiento: proteger la operación después del cierre", "Monitoring: protecting the deal after closing"), ["covenants", "kyc"], ""),
        ("04", ("Legal: contratos y gobierno de IA con estándar internacional", "Legal: contracts and AI governance to international standards"), ["contratos", "gobierno"], "alt"),
    ]
    for num, h, keys, cls in groups:
        body += section(num, t(*h), ai_cards(keys, light=True), cls=cls)
    principles = f'''<div class="principle">
      <div><b>{t("La IA acelera", "AI accelerates")}</b><p>{t("Lectura de documentos, conciliación de cifras y cruce de información en horas, no en semanas.", "Document reading, figure reconciliation and data matching in hours, not weeks.")}</p></div>
      <div><b>{t("El criterio es humano", "Judgment is human")}</b><p>{t("Cada conclusión la valida y la firma un profesional con experiencia en banca y derecho financiero.", "Every conclusion is validated and signed off by a professional experienced in banking and financial law.")}</p></div>
      <div><b>{t("La información es confidencial", "Information stays confidential")}</b><p>{t("Trabajamos bajo acuerdo de confidencialidad y compartimos con terceros solo lo que el cliente autoriza.", "We work under NDA and share with third parties only what the client authorizes.")}</p></div>
    </div>'''
    body += section("05", t("Tres principios en todos nuestros servicios con IA", "Three principles across all our AI services"), principles, cls="dark")
    body += contact_band()
    page("/inteligencia-artificial/", "ia", "IA aplicada · Venegas Capital Group", "Applied AI · Venegas Capital Group",
         "Diagnóstico de bancabilidad exprés, data room inteligente, matching de fondeadores, analítica de cartera, monitoreo de covenants, KYC/AML, revisión contractual y gobierno de IA.", body)


def build_firm():
    body = hero(t("La firma", "The firm"),
                t("Banca de inversión y derecho financiero <em>en un mismo equipo</em>", "Investment banking and financial law <em>in one team</em>"),
                p("Venegas Capital Group nace de 18 años de experiencia estructurando operaciones en Latinoamérica, Estados Unidos y Europa, y de la convicción de que una operación bien estructurada se aprueba más rápido y en mejores condiciones.",
                  "Venegas Capital Group draws on 18 years of structuring transactions across Latin America, the United States and Europe, and on the conviction that a well-structured transaction gets approved faster and on better terms.", "lead"),
                page_cls=" page")
    about = f'''<div class="about">
      <div>
        {p("Rodrigo Venegas es abogado y banquero de inversión con más de 18 años en banca privada, estructuración financiera, fusiones y adquisiciones y levantamiento de capital en Latinoamérica, Estados Unidos y Europa. Ha participado en transacciones que superan los USD 300 millones en energía, farmacéutico, activos reales e inmobiliario.", "Rodrigo Venegas is a lawyer and investment banker with more than 18 years in private banking, financial structuring, M&A and capital raising across Latin America, the United States and Europe. He has worked on transactions exceeding USD 300 million in energy, pharma, real assets and real estate.")}
        {p("Su trabajo consiste en convertir una empresa o un proyecto en una oportunidad financiable: ordenar la información, identificar los riesgos antes que el banco o el fondo, diseñar la estructura adecuada y acompañar el proceso hasta el cierre, con los documentos legales incluidos.", "His work is to turn a company or project into a financeable opportunity: organize the information, identify risks before the bank or fund does, design the right structure and support the process through closing, legal documents included.")}
        {p("Como emprendedor ha fundado más de diez empresas, con dos ventas exitosas, y fue pionero de la tokenización de activos en la región. Hoy integra la inteligencia artificial en la práctica para acelerar el due diligence, la modelación y el análisis multijurisdiccional sin sacrificar el criterio profesional.", "As an entrepreneur he has founded more than ten companies, with two successful exits, and was a pioneer of asset tokenization in the region. Today he integrates artificial intelligence into the practice to accelerate due diligence, modeling and multi-jurisdictional analysis without compromising professional judgment.")}
      </div>
      <aside class="callout">
        <h3>{t("Formación y credenciales", "Education & credentials")}</h3>
        <ul>
          <li><b>{t("Abogado", "Law degree (LL.B.)")}</b> — Universidad de La Sabana</li>
          <li><b>EMBA</b> — Quantic School of Business and Technology, Washington D.C.</li>
          <li><b>Blockchain &amp; DApps</b> — {t("certificación", "certification")}</li>
          <li><b>{t("IA: desarrollo y gobernanza", "AI development &amp; governance")}</b> — {t("certificaciones Anthropic y Gemini", "Anthropic and Gemini certifications")}</li>
          <li><b>{t("Idiomas", "Languages")}</b> — {t("Español nativo · Inglés C2", "Native Spanish · C2 English")}</li>
        </ul>
        <a class="li-card" href="{LINKEDIN}" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" width="40" height="40" fill="#A8894B" aria-hidden="true">{LI_PATH}</svg>
          <div><b>RODRIGO VENEGAS</b><small>{t("Socio director · Venegas Capital Group", "Managing partner · Venegas Capital Group")}</small><span class="go">{t("Ver perfil en LinkedIn →", "View LinkedIn profile →")}</span></div>
        </a>
      </aside>
    </div>'''
    body += section("01", t("Rodrigo Venegas, socio director", "Rodrigo Venegas, managing partner"), about)
    rows = [
        (("Energía", "Energy"), ("Estructuración y levantamiento de capital para proyectos de generación, incluida energía solar; venta de portafolios de activos solares a compradores estratégicos; fundación y venta de una compañía de energía.", "Structuring and capital raising for generation projects, including solar; sale of solar asset portfolios to strategic buyers; founded and sold an energy company.")),
        (("Farmacéutico", "Pharma"), ("Consolidación de deuda y elegibilidad crediticia ante banca internacional y panameña.", "Debt consolidation and credit eligibility with international and Panamanian banks.")),
        (("Inmobiliario y construcción", "Real estate & construction"), ("Conceptos de bancabilidad, vehículos fiduciarios y estructuración de proyectos multifamiliares y comerciales.", "Bankability opinions, trust vehicles and structuring of multifamily and commercial projects.")),
        (("Servicios financieros", "Financial services"), ("Originadoras de crédito, factoring y libranza: due diligence, sustitución de fondeo, compradores de cartera y titularización.", "Credit, factoring and payroll-lending originators: due diligence, funding replacement, loan-book buyers and securitization.")),
        (("Activos reales y logística", "Real assets & logistics"), ("Capital de trabajo, consolidación de pasivos y referidos a banca empresarial.", "Working capital, liability consolidation and corporate-banking referrals.")),
    ]
    trs = "".join(f"<tr><td>{t(*a)}</td><td>{t(*b)}</td></tr>" for a, b in rows)
    table = (f'<table class="t"><thead><tr><th>{t("Sector", "Sector")}</th><th>{t("Tipo de trabajo", "Type of work")}</th></tr></thead><tbody>{trs}</tbody></table>'
             f'<p style="font-size:14px;color:var(--gris);margin-top:12px">{t("Volumen agregado de transacciones:", "Aggregate transaction volume:")} <b style="color:var(--verde-medio)">USD 300M+</b></p>')
    body += section("02", t("Experiencia en los sectores donde la estructura define el resultado", "Experience in the sectors where structure defines the outcome"), table, cls="alt")
    ventures = [
        (("Fundador · Exit", "Founder · Exit"), "Blackstorm Energy", ("Compañía de energía adquirida por Empire Diversified Energy LLC, donde luego fue VP Latin America.", "Energy company acquired by Empire Diversified Energy LLC, where he later served as VP Latin America.")),
        (("Fundador · Exit", "Founder · Exit"), "Agaia Latam", ("Empresa de nanotecnología fundada, desarrollada y vendida.", "Nanotechnology company founded, built and sold.")),
        (("Fundador · Pionero", "Founder · Pioneer"), "Fidunova", ("Primera plataforma de tokenización fiduciaria de América Latina, sobre Algorand. Proyecto adelantado a su mercado, hoy cerrado.", "Latin America's first fiduciary tokenization platform, on Algorand. A project ahead of its market, now closed.")),
        (("Fundador · Pionero", "Founder · Pioneer"), "Wiracoxa", ("Ecosistema blockchain con billeteras digitales y stablecoins. Proyecto adelantado a su mercado, hoy cerrado.", "Blockchain ecosystem with digital wallets and stablecoins. A project ahead of its market, now closed.")),
    ]
    vs = "".join(f'<div class="venture"><div class="tag">{t(*tg)}</div><h3>{n}</h3><p>{t(*d)}</p></div>' for tg, n, d in ventures)
    body += section("03", t("Emprendedor antes que asesor: más de diez empresas fundadas", "An entrepreneur before an advisor: more than ten companies founded"), f'<div class="ventures">{vs}</div>')
    body += contact_band()
    page("/firma/", "firma", "La firma · Venegas Capital Group", "The firm · Venegas Capital Group",
         "Rodrigo Venegas, socio director: abogado y banquero de inversión con más de 18 años y USD 300M+ en transacciones estructuradas.", body)


def build_contact():
    body = hero(t("Contacto", "Contact"),
                t("Conversemos sobre <em>su operación</em>", "Let's talk about <em>your transaction</em>"),
                p("Cuéntenos qué necesita: crédito, capital, vender o comprar una empresa o un activo, liquidez sobre su cartera o fondeo internacional. En una primera llamada de 30 minutos le decimos si la operación está lista y qué le falta.",
                  "Tell us what you need: credit, capital, selling or buying a company or asset, liquidity on your receivables or international funding. In a first 30-minute call we tell you whether the transaction is ready and what it still needs.", "lead"),
                ctas=False, page_cls=" page")
    prep = [
        ("Estados financieros de los dos últimos años y el corte más reciente", "Financial statements for the last two years and the latest interim figures"),
        ("Monto, plazo y destino de los recursos que necesita", "Amount, tenor and use of the funds you need"),
        ("Deuda actual: entidad, saldo, tasa y garantías", "Current debt: lender, balance, rate and collateral"),
        ("Para proyectos o activos: licencias, avance y estudios técnicos", "For projects or assets: permits, progress and technical studies"),
    ]
    lis = "".join(f"<li>{t(*x)}</li>" for x in prep)
    body += f'''<section class="block contact">
  <div class="wrap">
    <div class="band"><span class="num">01</span><span class="rule"></span></div>
    <h2>{t("Elija el canal que prefiera", "Choose the channel you prefer")}</h2>
    {contact_tiles()}
  </div>
</section>'''
    body += section("02", t("Para aprovechar mejor la primera llamada", "To make the most of the first call"),
                    f'<div class="two"><ul class="checks">{lis}</ul><div class="panel"><h3>{t("Confidencialidad", "Confidentiality")}</h3><p style="font-size:16.5px">{t("Si lo prefiere, firmamos un acuerdo de confidencialidad antes de recibir cualquier documento.", "If you prefer, we sign an NDA before receiving any document.")}</p></div></div>',
                    cls="alt", intro=("No es obligatorio, pero si tiene esta información a mano podemos darle un primer diagnóstico en la misma conversación.",
                                      "It is not required, but if you have this information at hand we can give you a first diagnosis in the same conversation."))
    page("/contacto/", "contacto", "Contacto · Venegas Capital Group", "Contact · Venegas Capital Group",
         "Agende una llamada de 30 minutos con Venegas Capital Group. Bogotá · Panamá · Miami.", body)


def build_404():
    body = hero("404", t("Esta página <em>no existe</em>", "This page <em>does not exist</em>"),
                p("Es posible que el enlace haya cambiado. Vuelva al inicio o revise nuestros servicios.", "The link may have changed. Go back home or browse our services.", "lead"),
                page_cls=" page")
    page("/404.html", "", "Página no encontrada · Venegas Capital Group", "Page not found · Venegas Capital Group", "Página no encontrada.", body)


def build_meta(paths):
    urls = "".join(f"<url><loc>{DOMAIN}{u}</loc></url>" for u in paths)
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")


if __name__ == "__main__":
    build_home()
    build_services_index()
    for s in ALL_SERVICES:
        build_service(s)
    build_ai()
    build_firm()
    build_contact()
    build_404()
    paths = ["/", "/servicios/"] + [f'/servicios/{s["slug"]}/' for s in ALL_SERVICES] + ["/inteligencia-artificial/", "/firma/", "/contacto/"]
    build_meta(paths)
    print("Generadas", len(paths) + 1, "páginas")
