import json
import math

with open("../../config.json", "r") as file:
    config = json.load(file)

dev_time = config["economic_data"]["dev_time_months"]
if dev_time in [1, 21, 31]:
    dev_time_readable = f"{dev_time} месяц"
elif dev_time in [2, 3, 4, 22, 23, 24, 32, 33, 34]:
    dev_time_readable = f"{dev_time} месяца"
elif dev_time >= 0 and dev_time <= 36:
    dev_time_readable = f"{dev_time} месяцев"
else:
    raise ValueError(f"dev_time_months == {dev_time}?")

economic_loc_content = ""
estimate_loc = 0
actual_loc = 0
for loc in config["economic_data"]["lines_of_code"]:
    estimate_loc += loc["estimate"]
    actual_loc += loc["actual"]
    loc = [
        loc["func_code"],
        loc["func_name"],
        loc["estimate"],
        loc["actual"],
    ]
    economic_loc_content += " & ".join(map(str, loc)) + " \\\\ \\hline\n"

working_days_month = 22
dev_time_days = config["economic_data"]["dev_time_months"] * 30

value_ZP_osn = round(
    config["economic_data"]["base_rate"]
    * config["economic_data"]["dev_category_multiplier"]
    * dev_time_days
    * config["economic_data"]["premium_coefficient"]
    / working_days_month
)

value_ZP_dop = round(
    value_ZP_osn * config["economic_data"]["extra_payment_percents"] / 100
)

value_ZP = value_ZP_osn + value_ZP_dop
value_Rsoc = round(value_ZP * 0.35)
value_R_m = round(value_ZP_osn * config["economic_data"]["material_percents"] / 100)

value_R_mv = round(
    config["economic_data"]["machine_hour_cost"]
    * actual_loc
    * config["economic_data"]["debug_portion"]
    / 100
)

value_R_nr = round(
    config["economic_data"]["other_spends_percents"] * value_ZP_osn / 100
)

value_SR = (
    value_ZP_osn + value_ZP_dop + value_Rsoc + value_R_m + value_R_mv + value_R_nr
)

value_Ro = round(value_SR * config["economic_data"]["usage_spends_percents"] / 100)
value_Rso = round(value_SR * config["economic_data"]["support_spends_percents"] / 100)

value_SP = value_SR + value_Ro + value_Rso

value_P = round(value_SP * config["economic_data"]["profitability_percents"] / 100)

value_Cp = value_SP + value_P

value_NDS_pp = round(value_Cp * config["economic_data"]["tax_percents"] / 100)

value_Co = value_SP + value_P + value_NDS_pp

value_PC = round(value_P * (1 - (config["economic_data"]["income_tax_percents"] / 100)))

with open("../config/env.sty", "w") as file:
    # config['department']['']
    recendentMoreInfo = "\n    ".join(config["recendent"]["moreInfo"])
    file.write(
        f"""\def \envDiplomMinistr {{{config['ministry']}}}
\def \envDiplomEducation {{{config['education']}}}
\def \envDiplomUniversity {{{config['university']}}}
\def \envDiplomCathedra {{{config['cathedra']}}}

\def \envDiplomTitle {{{config['title']}}}
\def \envDiplomEnterprice {{{config['enterprise']}}}
\def \envDiplomNumber {{{config['number']}}}
\def \envDiplomVersion {{{config['version']}}}

\def \envDiplomCity {{{config['city']}}}

\def \envDiplomStudentGroupName {{{config['student']['groupName']}}}
\def \envDiplomStudentGroupNumber {{{config['student']['groupNumber']}}}
\def \envDiplomStudentCard {{{config['student']['card']}}}

\def \envDiplomStudentSurname {{{config['student']['surname']}}}
\def \envDiplomStudentInitials {{{config['student']['initials']}}}
\def \envDiplomStudentInfo{{{config['student']['info']}}}

% Руководитель
\def \envDiplomTeacherSurname {{{config['teacher']['surname']}}}
\def \envDiplomTeacherInitials {{{config['teacher']['initials']}}}
\def \envDiplomTeacherInfo{{{config['teacher']['info']}}}

% Консультант по экономическому разделу
\def \envDiplomEconomicSurname {{{config['economic']['surname']}}}
\def \envDiplomEconomicInitials {{{config['economic']['initials']}}}
\def \envDiplomEconomicInfo{{{config['economic']['info']}}}

% Консультант по ЕСПД
\def \envDiplomEspdSurname {{{config['espd']['surname']}}}
\def \envDiplomEspdInitials {{{config['espd']['initials']}}}
\def \envDiplomEspdInfo{{{config['espd']['info']}}}

% Рецензент
\def \envDiplomRecendentSurname {{{config['recendent']['surname']}}}
\def \envDiplomRecendentInitials {{{config['recendent']['initials']}}}
\def \envDiplomRecendentInfo{{{config['recendent']['info']}}}
\def \envDiplomRecendentMoreInfo{{\n    {recendentMoreInfo}\n}}

\def \envDiplomHeadCathedraSurname{{{config['department']['surname']}}}
\def \envDiplomHeadDepartmentInitials{{{config['department']['initials']}}}
\def \envDiplomHeadDepartmentInfo {{{config['department']['info']}}}

% Экономический раздел
\def \envGPREstimateLOC {{{estimate_loc}}}
\def \envGPRActualLOC {{{actual_loc}}}
\def \envGPRDevTimeMonth {{{config["economic_data"]["dev_time_months"]}}}
\def \envGPRDevTimeMonthReadable {{{dev_time_readable}}}
\def \envGPRDevTimeDays {{{dev_time_days}}}
\def \envGPRWorkingDaysInMonth{{{working_days_month}}}
\def \envGPRBaseRate {{{config["economic_data"]["base_rate"]}}}
\def \envGPRDevCategory {{{config["economic_data"]["dev_category"]}}}
\def \envGPRDevCategoryMultiplier {{{config["economic_data"]["dev_category_multiplier"]}}}
\def \envGPRPremiumCoefficient {{{config["economic_data"]["premium_coefficient"]}}}
\def \envGPRValueZPosn {{{value_ZP_osn}}}
\def \envGPRExtraPaymentPercents {{{config["economic_data"]["extra_payment_percents"]}}}
\def \envGPRValueZPdop {{{value_ZP_dop}}}
\def \envGPRValueZP {{{value_ZP}}}
\def \envGPRValueRsoc {{{value_Rsoc}}}
\def \envGPRMaterialPercents {{{config["economic_data"]["material_percents"]}}}
\def \envGPRValueRm {{{value_R_m}}}
\def \envGPRMachineHourCost {{{config["economic_data"]["machine_hour_cost"]}}}
\def \envGPRDebugPortion {{{config["economic_data"]["debug_portion"]}}}
\def \envGPRValueRmv {{{value_R_mv}}}
\def \envGPROtherSpendsPercents {{{config["economic_data"]["other_spends_percents"]}}}
\def \envGPRValueRnr {{{value_R_nr}}}
\def \envGPRValueSR {{{value_SR}}}
\def \envGPRUsageSpendsPercents {{{config["economic_data"]["usage_spends_percents"]}}}
\def \envGPRValueRo {{{value_Ro}}}
\def \envGPRSupportSpendsPercents {{{config["economic_data"]["support_spends_percents"]}}}
\def \envGPRValueRso {{{value_Rso}}}
\def \envGPRValueSP {{{value_SP}}}
\def \envGPRProfitabilityPercents {{{config["economic_data"]["profitability_percents"]}}}
\def \envGPRValueP {{{value_P}}}
\def \envGPRValueCp {{{value_Cp}}}
\def \envGPRTaxPercents {{{config["economic_data"]["tax_percents"]}}}
\def \envGPRValueNDSpp {{{value_NDS_pp}}}
\def \envGPRValueCo {{{value_Co}}}
\def \envGPRIncomeTaxPercents {{{config["economic_data"]["income_tax_percents"]}}}
\def \envGPRValuePC {{{value_PC}}}





% Прочее
\def \envDiplomDateInput{{<<\\underline{{\hspace{{0.5cm}}}}>> \\underline{{\hspace{{2cm}}}} \ESKDtheYear~г.}}
\def \\No {{\\textnumero}}
\date {{{config["year"]}/месяц/день}}
"""
    )

with open("../config/economic_loc.tex", "w") as file:
    file.write(economic_loc_content)
