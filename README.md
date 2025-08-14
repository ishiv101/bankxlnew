# bankxlnew

# Read me first

This is my first repo!

I want to learn to use GitHub!

A virtual finance internship platform with AI, case studies, and certification.


import random
import re
import time

app = Flask(__name__)

# -------------------------------
# In-memory state (simple demo DB)
# -------------------------------
AVATAR_OPTIONS = [
    "🧑‍💼 Business Person",
    "👩‍💻 Software engineer",
    "🧑‍🎓 Analyst",
    "🧑‍🔬 Strategist"
]

MEETING_TYPES = ["Client Meeting", "Investor Update", "Legal Review", "Internal Sync"]

SAMPLE_COMPANY_DATA = {
    "FutureTech Inc.": {
        "revenue": 850.3, "net_income": 110.9, "total_assets": 3000.2,
        "total_debt": 620.6, "equity": 2379.6
    },
    "Global Consumer Goods": {
        "revenue": 1450.0, "net_income": 180.4, "total_assets": 4200.0,
        "total_debt": 1200.0, "equity": 3000.0
    },
    "Sustainable Energy Co.": {
        "revenue": 620.7, "net_income": 72.1, "total_assets": 1900.0,
        "total_debt": 500.0, "equity": 1400.0
    },
}
COMPANY_NAMES = list(SAMPLE_COMPANY_DATA.keys())

avatars = {}             # user_id -> avatar string
meetings = []            # list of dicts
whiteboard_data = []     # list of {"user_id", "content", "timestamp"}
user_task_index = {}     # user_id -> int
tasks = [
    "Build 3-statement model",
    "Draft client memo",
    "Run comps analysis",
    "Join due diligence call",
    "Update investor presentation"
]

# -------------------------------
# Utility generators / helpers
# -------------------------------
def rnd(a, b, nd=2): return round(random.uniform(a, b), nd)

def generate_random_financial_statement(company_name, statement_type=None):
    """Generates a random simplified financial statement. If statement_type is None, choose one."""
    if statement_type is None:
        statement_type = random.choice(["Income Statement", "Balance Sheet", "Cash Flows"])
    data = {"Company": company_name, "Type": statement_type}

    if statement_type == "Income Statement":
        data["Revenue"] = rnd(100, 1000)
        data["Cost of Goods Sold"] = rnd(data["Revenue"] * 0.4, data["Revenue"] * 0.7)
        data["Gross Profit"] = round(data["Revenue"] - data["Cost of Goods Sold"], 2)
        data["Operating Expenses"] = rnd(data["Gross Profit"] * 0.1, data["Gross Profit"] * 0.3)
        data["Operating Income"] = round(data["Gross Profit"] - data["Operating Expenses"], 2)
        data["Interest Expense"] = rnd(data["Operating Income"] * 0.01, data["Operating Income"] * 0.05)
        data["Income Before Tax"] = round(data["Operating Income"] - data["Interest Expense"], 2)
        data["Income Tax"] = rnd(data["Income Before Tax"] * 0.2, data["Income Before Tax"] * 0.3)
        data["Net Income"] = round(data["Income Before Tax"] - data["Income Tax"], 2)

    elif statement_type == "Balance Sheet":
        data["Assets"] = rnd(200, 2000)
        data["Current Assets"] = rnd(data["Assets"] * 0.3, data["Assets"] * 0.6)
        data["Non-Current Assets"] = round(data["Assets"] - data["Current Assets"], 2)
        data["Liabilities"] = rnd(data["Assets"] * 0.2, data["Assets"] * 0.7)
        data["Current Liabilities"] = rnd(data["Liabilities"] * 0.4, data["Liabilities"] * 0.8)
        data["Non-Current Liabilities"] = round(data["Liabilities"] - data["Current Liabilities"], 2)
        data["Equity"] = round(data["Assets"] - data["Liabilities"], 2)

    elif statement_type == "Cash Flows":
        data["Net Income"] = rnd(10, 100)
        data["Depreciation & Amortization"] = rnd(data["Net Income"] * 0.1, data["Net Income"] * 0.3)
        data["Change in Working Capital"] = rnd(data["Net Income"] * -0.2, data["Net Income"] * 0.2)
        data["Cash from Operations"] = round(
            data["Net Income"] + data["Depreciation & Amortization"] + data["Change in Working Capital"], 2)
        data["Capital Expenditures"] = -rnd(abs(data["Cash from Operations"]) * 0.2, abs(data["Cash from Operations"]) * 0.5)
        data["Cash from Investing"] = round(data["Capital Expenditures"], 2)
        data["Proceeds from Debt"] = rnd(0, 50)
        data["Repayment of Debt"] = -rnd(0, 30)
        data["Cash from Financing"] = round(data["Proceeds from Debt"] + data["Repayment of Debt"], 2)
        data["Net Change in Cash"] = round(data["Cash from Operations"] + data["Cash from Investing"] + data["Cash from Financing"], 2)
    return data

def format_statement_lines(d):
    return [f"- {k}: ${v:.2f} million" for k, v in d.items() if k not in ("Company","Type")]

# -------------------------------
# Avatar
# -------------------------------
@app.post("/choose_avatar")
def choose_avatar():
    data = request.get_json(force=True)
    user_id = data.get("user_id")
    avatar = data.get("avatar_url") or data.get("avatar")  # allow URL or label
    if not user_id or not avatar:
        return jsonify(error="Missing user_id or avatar"), 400
    avatars[user_id] = avatar
    return jsonify(message="Avatar selected!", user_id=user_id, avatar=avatar)

# -------------------------------
# Meetings
# -------------------------------
@app.post("/send_meeting_invite")
def send_meeting_invite():
    mtype = random.choice(["Client", "Investor", "Legal", "Internal"])
    meeting = {
        "id": len(meetings) + 1,
        "type": mtype,
        "start_time": datetime.utcnow().isoformat(),
        "message": f"You’ve been invited to a {mtype} meeting!"
    }
    meetings.append(meeting)
    return jsonify(meeting)

@app.get("/join_meeting/<int:meeting_id>")
def join_meeting(meeting_id):
    m = next((x for x in meetings if x["id"] == meeting_id), None)
    if not m:
        return jsonify(error="Meeting not found"), 404
    return jsonify(message=f"Joined {m['type']} meeting!", meeting=m)

# -------------------------------
# Whiteboard (text notes API)
# -------------------------------
@app.route("/whiteboard", methods=["GET","POST"])
def whiteboard():
    if request.method == "POST":
        data = request.get_json(force=True)
        user_id = data.get("user_id")
        content = data.get("content")
        if not user_id or not content:
            return jsonify(error="Missing user_id or content"), 400
        whiteboard_data.append({
            "user_id": user_id,
            "content": content,
            "timestamp": datetime.utcnow().isoformat()
        })
        return jsonify(message="Whiteboard updated")
    # GET
    return jsonify(whiteboard_data)

# -------------------------------
# Tasks (compatible with your fetch)
# GET /next-task?user=neha
# -------------------------------
@app.get("/next-task")
def next_task():
    user = request.args.get("user", "default")
    idx = user_task_index.get(user, 0)
    task = tasks[idx % len(tasks)]
    user_task_index[user] = idx + 1
    return jsonify(task=task, index=idx)

# -------------------------------
# Formula checker (your hints)
# POST /check_formula { "formula": "..." }
# -------------------------------
MISTAKE_HINTS = {
    "unmatched_parentheses": "Check for missing or extra parentheses.",
    "invalid_characters": "Formula contains invalid characters. Stick to variables, numbers, and operators.",
    "consecutive_operators": "Consecutive operators detected. Review your formula.",
    "missing_operator": "Possible missing operator between numbers or variables.",
    "division_by_zero": "Division by zero risk detected.",
    "unrecognized_variable": "Unrecognized variable used. Verify spelling.",
}
ALLOWED_VARIABLES = [
    "Revenue","COGS","OperatingExpenses","OperatingIncome","EBITDA","NetIncome",
    "GrossMargin","EBITDAMargin","NetMargin","DiscountRate","ExitMultiple",
    "DebtAmount","RevenueGrowth","CostOfGoodsSoldPercent","OperatingExpensesPercent",
]

@app.post("/check_formula")
def check_formula():
    data = request.get_json(force=True)
    formula = data.get("formula", "")
    hints = []

    if formula.count("(") != formula.count(")"):
        hints.append(MISTAKE_HINTS["unmatched_parentheses"])
    if re.search(r"[^a-zA-Z0-9\+\-\*/\.\(\)\s]", formula):
        hints.append(MISTAKE_HINTS["invalid_characters"])
    if re.search(r"[\+\-\*/]{2,}", formula.replace("**", "")):
        hints.append(MISTAKE_HINTS["consecutive_operators"])
    if re.search(r"\d[a-zA-Z]", formula) or re.search(r"[a-zA-Z]\d", formula):
        hints.append(MISTAKE_HINTS["missing_operator"])
    if re.search(r"/0(?!\d)", formula):
        hints.append(MISTAKE_HINTS["division_by_zero"])

    tokens = re.findall(r"[a-zA-Z_]+", formula)
    for token in tokens:
        if token not in ALLOWED_VARIABLES:
            hints.append(f"{MISTAKE_HINTS['unrecognized_variable']} → '{token}'")

    if not hints:
        hints.append("✅ No mistakes detected. Formula looks good!")
    return jsonify(hints=hints)

# -------------------------------
# Triggered finance generators
# POST /trigger { "user_id": "...", "text": "..." }
# -------------------------------
def trig_given_info_about_company():
    revenue_growth = rnd(0.05, 0.20, 2)
    ebitda_margin = rnd(0.10, 0.30, 2)
    exit_multiple = round(random.uniform(5.0, 12.0), 1)
    discount_rate = rnd(0.08, 0.15, 2)
    debt_mult = round(random.uniform(0.5, 3.0), 1)
    return (
        "Detected 'given info about the company'. Random inputs:\n"
        f"- Revenue Growth Rate: {revenue_growth}\n"
        f"- EBITDA Margin: {ebitda_margin}\n"
        f"- Exit Multiple: {exit_multiple}x\n"
        f"- Discount Rate: {discount_rate}\n"
        f"- Debt Amount (as multiple of EBITDA): {debt_mult}x\n"
    )

def trig_some_capital():
    company = random.choice(list(SAMPLE_COMPANY_DATA.keys()))
    d = SAMPLE_COMPANY_DATA[company]
    return (
        f"User triggered 'some capital'. Random company: {company}\n"
        f"- Revenue: ${d['revenue']:.2f}m\n"
        f"- Net Income: ${d['net_income']:.2f}m\n"
        f"- Total Assets: ${d['total_assets']:.2f}m\n"
        f"- Total Debt: ${d['total_debt']:.2f}m\n"
        f"- Equity: ${d['equity']:.2f}m\n"
    )

def trig_some_percent():
    company = random.choice(COMPANY_NAMES)
    gross_margin = rnd(0.40, 0.80, 2)
    op_margin = rnd(0.10, 0.40, 2)
    net_margin = rnd(0.05, 0.25, 2)
    rev_growth = rnd(-0.05, 0.20, 2)
    cogs_pct = round(1 - gross_margin, 2)
    opex_pct = round(gross_margin - op_margin, 2)
    return (
        f"'some %' → {company}\n"
        f"- Gross Margin: {gross_margin*100:.2f}%\n"
        f"- Operating Margin: {op_margin*100:.2f}%\n"
        f"- Net Profit Margin: {net_margin*100:.2f}%\n"
        f"- Revenue Growth Rate: {rev_growth*100:.2f}%\n"
        f"- COGS %: {cogs_pct*100:.2f}%\n"
        f"- Opex %: {opex_pct*100:.2f}%\n"
    )

def trig_selected():
    company = random.choice(COMPANY_NAMES)
    st = generate_random_financial_statement(company)
    lines = "\n".join(format_statement_lines(st))
    return f"'selected' → {st['Type']} for {company}\n{lines}"

def trig_all_three():
    company = random.choice(COMPANY_NAMES)
    inc = generate_random_financial_statement(company, "Income Statement")
    bal = generate_random_financial_statement(company, "Balance Sheet")
    cf  = generate_random_financial_statement(company, "Cash Flows")
    return (
        f"'Given all 3 statements' → {company}\n\n"
        f"--- Income Statement ---\n" + "\n".join(format_statement_lines(inc)) + "\n\n"
        f"--- Balance Sheet ---\n" + "\n".join(format_statement_lines(bal)) + "\n\n"
        f"--- Cash Flow Statement ---\n" + "\n".join(format_statement_lines(cf)) + "\n"
    )

def trig_some_dollar():
    company = random.choice(COMPANY_NAMES)
    revenue = rnd(50, 1000)
    cogs = rnd(revenue*0.4, revenue*0.7)
    opex = rnd(revenue*0.1, revenue*0.3)
    net_income = rnd(revenue*0.05, revenue*0.20)
    total_assets = rnd(100, 2000)
    total_liabilities = rnd(total_assets*0.2, total_assets*0.7)
    equity = round(total_assets - total_liabilities, 2)
    cfo = rnd(net_income*0.8, net_income*1.2)
    capex = -rnd(abs(cfo)*0.1, abs(cfo)*0.4)
    return (
        f"'some $' → {company}\n"
        f"- Revenue: ${revenue:.2f}m\n- COGS: ${cogs:.2f}m\n- Opex: ${opex:.2f}m\n"
        f"- Net Income: ${net_income:.2f}m\n- Total Assets: ${total_assets:.2f}m\n"
        f"- Total Liabilities: ${total_liabilities:.2f}m\n- Equity: ${equity:.2f}m\n"
        f"- CFO: ${cfo:.2f}m\n- Capex: ${capex:.2f}m\n"
    )

def trig_some_amount():
    # base then increase by factor
    company = random.choice(COMPANY_NAMES)
    # simple base numbers:
    base_rev = rnd(500, 1000)
    base_cogs = rnd(300, 600)
    factor = round(random.uniform(1.1, 1.5), 2)
    rev = round(base_rev * factor, 2)
    cogs = round(base_cogs * factor, 2)
    return (f"'some amount' → {company}\n"
            f"- Increase factor: {factor-1:.2%}\n- Revenue: ${rev:.2f}m\n- COGS: ${cogs:.2f}m")

def trig_depreciation():
    asset_cost = rnd(10_000, 1_000_000)
    salvage = rnd(asset_cost*0.05, asset_cost*0.2)
    life = random.randint(3, 10)
    units = random.randint(10_000, 100_000)
    total_units = units * random.randint(5, 15)
    sl = round((asset_cost - salvage) / life, 2) if life else 0
    uop = round(((asset_cost - salvage) / total_units) * units, 2) if total_units else 0
    ddb_rate = 2 / life if life else 0
    return (
        "'some amount of depreciation'\n"
        f"- Asset Cost: ${asset_cost:.2f}\n- Salvage: ${salvage:.2f}\n- Life: {life} yrs\n"
        f"- Units this year: {units} / total {total_units}\n"
        f"- Straight-line (approx): ${sl}\n- Units-of-production (approx): ${uop}\n"
        f"- DDB rate: {ddb_rate*100:.2f}%\n"
    )

def trig_sbc():
    company = random.choice(COMPANY_NAMES)
    expense = rnd(1, 50)
    st = random.choice(["Income Statement","Balance Sheet","Cash Flow Statement"])
    if st == "Income Statement":
        desc = (f"SBC expense ${expense}m recognized as opex → lowers EBIT and net income.")
    elif st == "Balance Sheet":
        desc = (f"SBC increases equity (APIC) over vesting; retained earnings fall via lower NI.")
    else:
        desc = ("Non-cash expense added back in CFO; cash impacts can appear in financing via issuances/buybacks.")
    return f"'stock-based compensation' → {company}, view: {st}\n- {desc}"

def trig_investment():
    name = f"Project {chr(random.randint(65,90))}"
    initial = -rnd(100_000, 1_000_000, 2)
    rate = round(random.uniform(0.08, 0.15), 3)
    years = random.randint(5, 10)
    cfs = [ rnd(initial*-0.1, initial*-0.3) for _ in range(years) ]  # positive cfs
    # metrics
    def npv(cash_flows, r, init):
        v = init
        for i, cf in enumerate(cash_flows, 1):
            v += cf / ((1+r)**i)
        return round(v, 2)
    def irr(cash_flows, init, it=100):
        lo, hi = -0.5, 0.5
        for _ in range(it):
            mid = (lo+hi)/2
            v = init + sum(cf/((1+mid)**(i+1)) for i, cf in enumerate(cash_flows))
            if v > 0: lo = mid
            else: hi = mid
            if abs(v) < 1e-3: return round(mid*100, 2)
        return None
    def payback(cash_flows, init):
        cum = -init
        for i, cf in enumerate(cash_flows, 1):
            cum += cf
            if cum >= 0: return i
        return None

    npv_val = npv(cfs+[cfs[-1]*random.uniform(5,10)], rate, initial)
    irr_val = irr(cfs, initial)
    pb = payback(cfs, initial)
    return (
        f"'given investment' → {name}\n"
        f"- Initial: {initial}\n- Discount Rate: {rate}\n- Years: {years}\n"
        f"- Cash Flows: {cfs}\n"
        f"- NPV: {npv_val}\n- IRR: {irr_val}%\n- Payback: {pb or 'Never'} yrs\n"
    )

def trig_given_cfs():
    company = random.choice(COMPANY_NAMES)
    cf = generate_random_financial_statement(company, "Cash Flows")
    return "'Given a cash flow statement'\n" + "\n".join(format_statement_lines(cf))

def trig_company_financials():
    company = random.choice(COMPANY_NAMES)
    inc = generate_random_financial_statement(company, "Income Statement")
    bal = generate_random_financial_statement(company, "Balance Sheet")
    cf  = generate_random_financial_statement(company, "Cash Flows")
    return (
      f"'Given company financial statements' → {company}\n\n"
      f"--- Income Statement ---\n" + "\n".join(format_statement_lines(inc)) + "\n\n"
      f"--- Balance Sheet ---\n" + "\n".join(format_statement_lines(bal)) + "\n\n"
      f"--- Cash Flow Statement ---\n" + "\n".join(format_statement_lines(cf)) + "\n"
    )

TRIGGERS = [
    (r"given info about the company", trig_given_info_about_company),
    (r"some capital", trig_some_capital),
    (r"some %", trig_some_percent),
    (r"\bselected\b", trig_selected),
    (r"Given all 3 statements", trig_all_three),
    (r"some \$", trig_some_dollar),
    (r"some amount of depreciation", trig_depreciation),
    (r"some amount", trig_some_amount),
    (r"stock-based compensation", trig_sbc),
    (r"given investment", trig_investment),
    (r"Given a cash flow statement", trig_given_cfs),
    (r"Given company financial statements", trig_company_financials),
]

@app.post("/trigger")
def trigger_router():
    data = request.get_json(force=True)
    text = data.get("text","")
    for pattern, handler in TRIGGERS:
        if re.search(pattern, text, re.IGNORECASE):
            return jsonify(output=handler())
    return jsonify(output="No trigger matched.")

# -------------------------------
# Entry
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)