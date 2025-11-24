supported_turbines = {
    # ----------------------------
    # --- distributed turbines ---
    # ----------------------------
    'SWIFT_1kW': 'SWIFT_1kW_2.1', 
    'Pika_1.5kW': 'PikaT701_1.5kW_3', 
    'Skystream_2.1kW': 'Skystream3.7_2.1kW_3.7', 
    'Kestrele_2.5kW': 'Kestrele400nb_2.5kW_4',
    'Fortis_3.31kW': 'FortisMontana_3.31kW_5.04', 
    'SD6_5.2kW': 'SD6_5.2kW_5.5', 
    'Jacobs_12kW': 'Jacobs31-20_12kW_9.45', 
    'Bestwind_27.2kW': 'Bestwind30_27.2kW_13.1', 
    'Entegrity_50kW': 'EntegrityEW50_50kW_15', 
    'Ghrepower_61.2kW': 'GhrepowerFD21-50_61.2kW_21.5', 
    # EWT
    'EWT_52_900kW': 'EWT_DW52_900kW_51.5', 
    'EWT_54_900kW': 'EWT_DW54_900kW_54', 
    'EWT_54_1MW': 'EWT_DW54X_1MW_54.1', 
    'EWT_58_1MW': 'EWT_DW58_1MW_58', 
    'EWT_61_1MW': 'EWT_DW61_1MW_60.9', 
    # NPS
    'NPS_60kW': 'NPS60C-24_60kW_24.4', 
    'NPS_C27_90kW': 'NPS100C-27_90kW_27.4', 
    'NPS_C28_90kW': 'NPS100C-28_90kW_27.6',
    'NPS_C28_90_kW': 'NPS100C-28_90kW_28', 
    'NPS_B24_95kW': 'NPS100B-24_95kW_23.6', 
    'NPS_C24_95kW': 'NPS100C-24_95kW_24.4', 
    'NPS_B24C_95kW': 'NPS100B-24C_95kW_24.4', # missing rating, missing rotor diameter
    'NPS_C21_100kW': 'NPS100C-21_100kW_20.7', 
    'NPS_B21_100kW': 'NPS100B-21_100kW_20.7',  
    # CF
    'CF_10kW': 'CF10A_10kW_11.15', 
    'CF_11kW': 'CF11_11kW_9.36', 
    'CF_A_11kW': 'CF11A_11kW_11.15', 
    'CF_15kW': 'CF15_15kW_11.15', 
    'CF_20kW': 'CF20_20kW_13.1', 
    # Vestas
    'Vestas_V27_225kW': 'VestasV27_225kW_27', 
    'Vestas_V29_225kW': 'VestasV29_225kW_29', 
    # Bergey
    'Bergey_8.9kW': 'BergeyExcel10_8.9kW_7', 
    'Bergey_15.6kW': 'BergeyExcel15_15.6kW_9.6',  
    # COE
    'COE_20kW': '2019COE_DW20_20kW_12.4', 
    'COE_100kW': '2019COE_DW100_100kW_27.6', 
    # ----------------------------
    # ---- offshore turbines ----
    # ----------------------------
    'WTK_offshore': 'WTK_Validation_offshore_normalized', # missing power curve, missing rotor diameter
    'LEANWIND_8MW': 'LEANWIND_Reference_8MW_164', 
    # NREL
    'NREL_5MW': 'NREL_Reference_5MW_126', 
    # NREL 2019
    'NREL_2019_12MW': '2019ORCost_NREL_Reference_12MW_222',
    'NREL_2019_15MW': '2019ORCost_NREL_Reference_15MW_248',
    # NREL 2020 ATB
    'NREL_12MW': '2020ATB_NREL_Reference_12MW_214', 
    'NREL_15MW': '2020ATB_NREL_Reference_15MW_240', 
    'NREL_18MW': '2020ATB_NREL_Reference_18MW_263', 
    # NREL 2016
    'NREL_2016_6MW': '2016CACost_NREL_Reference_6MW_155',
    'NREL_2016_8MW': '2016CACost_NREL_Reference_8MW_180',  
    'NREL_2016_10MW': '2016CACost_NREL_Reference_10MW_205', 
    # IEA
    'IEA_15MW': 'IEA_Reference_15MW_240', 
    'DTU_10MW': 'DTU_Reference_v1_10MW_178', 
    'IEA_10MW': 'IEA_Reference_10MW_198', 
    # ----------------------------
    # ----- onshore turbines -----
    # ----------------------------
    # GE
    'GE_1.5MW': 'DOE_GE_1.5MW_77', 
    # NREL
    'NREL_3MW': '2023NREL_Bespoke_3MW_127.5', 
    'NREL_3.3MW': '2023NREL_Bespoke_3.3MW_148', 
    'NREL_4MW': '2020ATB_NREL_Reference_4MW_150', 
    'NREL_5.5MW': '2020ATB_NREL_Reference_5.5MW_175', 
    'NREL_6MW_196': '2023NREL_Bespoke_6MW_196', 
    'NREL_6MW_170': '2023NREL_Bespoke_6MW_170', 
    'NREL_7MW': '2020ATB_NREL_Reference_7MW_200', 
    'NREL_8.3MW': '2023NREL_Bespoke_8.3MW_196', 
    # COE
    'COE_2.3MW': '2017COE_Market_Average_2.3MW_113', 
    'COE_2.4MW': '2018COE_Market_Average_2.4MW_116', 
    'COE_2.6MW': '2019COE_Market_Average_2.6MW_121', 
    # IEA
    'IEA_3.4MW': 'IEA_Reference_3.4MW_130', 
    # Vestas
    'Vestas_660kW': 'VestasV47_660kW_47',
    'Vestas_1.65MW': 'VestasV82_1.65MW_82',  
    # BAR
    'BAR_BAU_3.25MW': 'BAR_BAU_LowSP_3.25MW_166', 
    'BAR_BAU_3.3MW': 'BAR_BAU-LBNL-IEA_3.3MW_156', 
    'BAR_4.5MW': 'BAR_LowSP_4.5MW_194', 
    'BAR_HighSP_5MW': 'BAR_HighSP_5.0MW_134.9', 
    'BAR_BAUa_5MW': 'BAR_BAUa_5.0MW_167.4', 
    'BAR_BAU_6.5MW': 'BAR_LowSP_6.5MW_234', 
    # IEC
    'IEC_Class1': 'IEC_Class1_Normalized_Industry_Composite', # missing specs, missing rating, missing rotor diameter
    'IEC_Class2': 'IEC_Class2_Normalized_Industry_Composite', # missing specs, missing rating, missing rotor diameter
    'IEC_Class3': 'IEC_Class3_Normalized_Industry_Composite', # missing specs, missing rating, missing rotor diameter
    # WTK_Validation
    'WTK_Class1': 'WTK_Validation_IEC-1_normalized', # missing power curve, missing rotor diameter
    'WTK_Class2': 'WTK_Validation_IEC-2_normalized', # missing power curve, missing rotor diameter
    'WTK_Class3': 'WTK_Validation_IEC-3_normalized', # missing power curve, missing rotor diameter
}

missing_information_turbines = [
    "WTK_Class1",
    "WTK_Class2",
    "WTK_Class3",
    "IEC_Class1",
    "IEC_Class2",
    "IEC_Class3",
    "WTK_offshore",
    "NPS_B24C_95kW"
]