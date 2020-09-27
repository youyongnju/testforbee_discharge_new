#!/usr/bin/env python

# common use

FDD_Band_Ch_UL_5M = {'B1_low': 1922.5e6, 'B1_Mid': 1950e6, 'B1_High': 1977.5e6,
                     'B2_low': 1852.5e6, 'B2_Mid': 1980e6, 'B2_High': 1907.5e6,
                     'B3_low': 1921e6, 'B3_Mid': 1925e6, 'B3_High': 1955e6,
                     'B4_low': 1920.5e6, 'B4_Mid': 1920.5e6, 'B4_High': 1920.5e6,
                     'B5_low': 826.5e6, 'B5_Mid': 836.5e6, 'B5_High': 846.5e6,
                     'B7_low': 1920.5e6, 'B7_Mid': 1920.5e6, 'B7_High': 1920.5e6,
                     'B8_low': 885.5e6, 'B8_Mid': 897.5e6, 'B8_High': 900.5e6,
                     'B20_low': 1920.5e6, 'B20_Mid': 1920.5e6, 'B20_High': 1920.5e6}

FDD_Band_Ch_UL_10M = {'B1_low': 1925e6, 'B1_Mid': 1950e6, 'B1_High': 1975e6,
                      'B2_low': 1855e6, 'B2_Mid': 1880e6, 'B2_High': 1905e6,
                      'B3_low': 1944e6, 'B3_Mid': 1945e6, 'B3_High': 1947e6,
                      'B4_low': 1920.5e6, 'B4_Mid': 1920.5e6, 'B4_High': 1920.5e6,
                      'B5_low': 829e6,    'B5_Mid': 836.5e6, 'B5_High': 844e6,
                      'B7_low': 1920.5e6, 'B7_Mid': 1920.5e6, 'B7_High': 1920.5e6,
                      'B8_low': 890e6, 'B8_Mid': 897.5e6, 'B8_High': 902e6,
                      'B20_low': 1920.5e6, 'B20_Mid': 1920.5e6, 'B20_High': 1920.5e6}

FDD_Band_Ch_UL_15M = {'B1_low': 1927.5e6, 'B1_Mid': 1950e6, 'B1_High': 1972.5e6,
                      'B2_low': 1920.5e6, 'B2_Mid': 1920.5e6, 'B2_High': 1920.5e6,
                      'B3_low': 1920.5e6, 'B3_Mid': 1920.5e6, 'B3_High': 1920.5e6,
                      'B4_low': 1920.5e6, 'B4_Mid': 1920.5e6, 'B4_High': 1920.5e6,
                      'B5_low': 830e6, 'B5_Mid': 836.5e6, 'B5_High': 840e6,
                      'B7_low': 1920.5e6, 'B7_Mid': 1920.5e6, 'B7_High': 1920.5e6,
                      'B8_low': 891e6, 'B8_Mid': 897.5e6, 'B8_High': 903e6,
                      'B20_low': 1920.5e6, 'B20_Mid': 1920.5e6, 'B20_High': 1920.5e6}

FDD_Band_Ch_UL_20M = {'B1_low': 1930e6, 'B1_Mid': 1950e6, 'B1_High': 1970e6,
                      'B2_low': 1920.5e6, 'B2_Mid': 1920.5e6, 'B2_High': 1920.5e6,
                      'B3_low': 1920.5e6, 'B3_Mid': 1920.5e6, 'B3_High': 1920.5e6,
                      'B4_low': 1920.5e6, 'B4_Mid': 1920.5e6, 'B4_High': 1920.5e6,
                      'B5_low': 832e6, 'B5_Mid': 836.5e6, 'B5_High': 839e6,
                      'B7_low': 1920.5e6, 'B7_Mid': 1920.5e6, 'B7_High': 1920.5e6,
                      'B8_low': 892e6, 'B8_Mid': 897.5e6, 'B8_High': 904e6,
                      'B20_low': 1920.5e6, 'B20_Mid': 1920.5e6, 'B20_High': 1920.5e6}

TDD_Band_Ch_5M = {'B34_low': 1920.5e6, 'B34_Mid': 1920.5e6, 'B34_High': 1920.5e6,
                     'B38_low': 1920.5e6, 'B38_Mid': 1920.5e6, 'B38_High': 1920.5e6,
                     'B39_low': 1920.5e6, 'B39_Mid': 1920.5e6, 'B39_High': 1920.5e6,
                     'B40_low': 2320e6, 'B40_Mid': 2350e6, 'B40_High': 2380e6,
                     'B41_low': 1920.5e6, 'B41_Mid': 1920.5e6, 'B41_High': 1920.5e6}

TDD_Band_Ch_10M = {'B34_low': 1920.5e6, 'B34_Mid': 1920.5e6, 'B34_High': 1920.5e6,
                      'B38_low': 1920.5e6, 'B38_Mid': 1920.5e6, 'B38_High': 1920.5e6,
                      'B39_low': 1920.5e6, 'B39_Mid': 1920.5e6, 'B39_High': 1920.5e6,
                      'B40_low': 2320e6, 'B40_Mid': 2350e6, 'B40_High': 2380e6,
                      'B41_low': 1920.5e6, 'B41_Mid': 1920.5e6, 'B41_High': 1920.5e6}

TDD_Band_Ch_15M = {'B34_low': 1920.5e6, 'B34_Mid': 1920.5e6, 'B34_High': 1920.5e6,
                      'B38_low': 1920.5e6, 'B38_Mid': 1920.5e6, 'B38_High': 1920.5e6,
                      'B39_low': 1920.5e6, 'B39_Mid': 1920.5e6, 'B39_High': 1920.5e6,
                      'B40_low': 2320e6, 'B40_Mid': 2350e6, 'B40_High': 2380e6,
                      'B41_low': 1920.5e6, 'B41_Mid': 1920.5e6, 'B41_High': 1920.5e6}

TDD_Band_Ch_20M = {'B34_low': 1920.5e6, 'B34_Mid': 1920.5e6, 'B34_High': 1920.5e6,
                      'B38_low': 1920.5e6, 'B38_Mid': 1920.5e6, 'B38_High': 1920.5e6,
                      'B39_low': 1920.5e6, 'B39_Mid': 1920.5e6, 'B39_High': 1920.5e6,
                      'B40_low': 2320e6, 'B40_Mid': 2350e6, 'B40_High': 2380e6,
                      'B41_low': 1920.5e6, 'B41_Mid': 1920.5e6, 'B41_High': 1920.5e6}