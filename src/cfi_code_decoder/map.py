CATEGORY_MAP = {
        'E': 'Equity',
        'C': 'Collective investment vehicles',
        'D': 'Debt instruments',
        'R': 'Entitlements',
        'O': 'Listed options',
        'F': 'Futures',
        'S': 'Swaps',
        'H': 'Non-listed and complex listed options',
        'I': 'Spot',
        'J': 'Forwards',
        'K': 'Strategies',
        'L': 'Financing',
        'T': 'Reference instruments',
        'M': 'Others',
    }

GROUP_MAP = {
        'E': {
            'S': "Common/Ordinary shares",
            'P': "Preferred/Preference shares",
            'C': "Common/Ordinary convertible shares",
            'F': "Preferred/Preference convertible shares",
            'L': "Limited partnership units",
            'D': "Depositary receipts on equities",
            'Y': "Structured instruments (participation)",
            'M': "Others",
        },
        'C': {
            'I': "Standard (vanilla) investment funds/mutual funds",
            'H': "Hedge funds",
            'B': "Real estate investment trusts (REITs)",
            'E': "Exchange-traded funds (ETFs)",
            'S': "Pension funds",
            'F': "Funds of funds",
            'P': "Private equity funds",
            'M': "Others",
        },
        'D': {
            'B': "Bonds",
            'C': "Convertible bonds",
            'W': "Bonds with warrants attached",
            'T': "Medium term notes",
            'S': "Structured products (capital protection)",
            'E': "Structured products (without capital protection)",
            'G': "Mortgage-backed securities",
            'A': "Asset-backed securities",
            'N': "Municipal bonds",
            'D': "Depositary receipts on debt instruments",
            'M': "Other",
            'Y': "Money Market Instruments",
        },
        'R': {
            'A': "Allotments (Bonus Rights)",
            'S': "Subscription Rights",
            'P': "Purchase Rights",
            'W': "Warrants",
            'F': "Mini-future certificates/constant leverage certificates",
            'D': "Depositary receipts on entitlements",
            'M': "Other",
        },
        'O': {
            'C': "Call options",
            'P': "Put options",
            'M': "Other",
        },
        'F': {
            'F': "Financial futures",
            'C': "Commodities futures",
        },
        'S': {
            'R': "Rates",
            'T': "Commodities",
            'E': "Equity",
            'C': "Credit",
            'F': "Foreign exchange",
            'M': "Other",
        },
        'H': {
            'R': "Rates",
            'T': "Commodities",
            'E': "Equity",
            'C': "Credit",
            'F': "Foreign exchange",
            'M': "Other",
        },
        'I': {
            'F': "Foreign exchange",
            'T': "Commodities",
        },
        'J': {
            'E': "Equity",
            'F': "Foreign exchange",
            'C': "Credit",
            'R': "Rates",
            'T': "Commodities",
        },
        'K': {
            'R': "Rates",
            'T': "Commodities",
            'E': "Equity",
            'C': "Credit",
            'F': "Foreign exchange",
            'Y': "Mixed assets",
            'M': "Other",
        },
        'L': {
            'L': "Loan-lease",
            'R': "Repurchase agreements",
            'S': "Securities lending",
        },
        'T': {
            'C': "Currencies",
            'T': "Commodities",
            'R': "Interest rates",
            'I': "Indices",
            'B': "Baskets",
            'D': "Stock dividends",
            'M': "Others",
        },
        'M': {
            'C': "Combined instruments",
            'M': "Other assets",
        },
    }

ATTRIBUTE_MAP = {
        ('E', 'S'): [  # Group ES: Common/Ordinary shares
            {
                "name": "voting_right",
                "mapping": {
                    'V': 'Voting',
                    'N': 'Non-Voting',
                    'R': 'Restricted',
                    'E': 'Enhanced voting'
                }
            },
            {
                "name": "ownership",
                "mapping": {
                    'T': 'Restrictions',
                    'U': 'Free'
                }
            },
            {
                "name": "payment_status",
                "mapping": {
                    'F': 'Fully Paid',
                    'O': 'Nil Paid',
                    'P': 'Partly Paid'
                }
            },
            {
                "name": "form",
                "mapping": {
                    'B': 'Bearer',
                    'R': 'Registered',
                    'N': 'Bearer/Registered',
                    'M': 'Others'
                }
            },
        ],
        ('E', 'P'): [  # Group EP: Preferred/Preference shares
            {
                "name": "voting_right",
                "mapping": {
                    'V': 'Voting',
                    'N': 'Non-Voting',
                    'R': 'Restricted',
                    'E': 'Enhanced voting'
                }
            },
            {
                "name": "redemption",
                "mapping": {
                    'R': 'Redeemable',
                    'E': 'Extendible',
                    'T': 'Redeemable/Extendible',
                    'G': 'Exchangeable',
                    'A': 'Redeemable/Exchangeable/Extendible',
                    'C': 'Redeemable/Exchangeable',
                    'N': 'Perpetual'
                }
            },
            {
                "name": "income",
                "mapping": {
                    'F': 'Fixed Rate Income',
                    'C': 'Cumulative, Fixed Rate Income',
                    'P': 'Participating Income',
                    'Q': 'Cumulative, Participating Income',
                    'A': 'Adjustable/Variable Rate Income',
                    'N': 'Normal Rate Income',
                    'U': 'Auction Rate Income',
                    'D': 'Dividends'
                }
            },
            {
                "name": "form",
                "mapping": {
                    'B': 'Bearer',
                    'R': 'Registered',
                    'N': 'Bearer/Registered',
                    'M': 'Others'
                }
            },
        ],
        ('E', 'C'): [  # Group EC: Common/Ordinary convertible shares
            {
                "name": "voting_right",
                "mapping": {
                    'V': 'Voting',
                    'N': 'Non-Voting',
                    'R': 'Restricted',
                    'E': 'Enhanced voting'
                }
            },
            {
                "name": "ownership",
                "mapping": {
                    'T': 'Restrictions',
                    'U': 'Free'
                }
            },
            {
                "name": "payment_status",
                "mapping": {
                    'F': 'Fully Paid',
                    'O': 'Nil Paid',
                    'P': 'Partly Paid'
                }
            },
            {
                "name": "form",
                "mapping": {
                    'B': 'Bearer',
                    'R': 'Registered',
                    'N': 'Bearer/Registered',
                    'M': 'Others'
                }
            },
        ],
        ('E', 'F'): [  # Group EF: Preferred/Preference convertible shares
            {
                "name": "voting_right",
                "mapping": {
                    'V': 'Voting',
                    'N': 'Non-Voting',
                    'R': 'Restricted',
                    'E': 'Enhanced voting'
                }
            },
            {
                "name": "redemption",
                "mapping": {
                    'R': 'Redeemable',
                    'E': 'Extendible',
                    'T': 'Redeemable/Extendible',
                    'G': 'Exchangeable',
                    'A': 'Redeemable/Exchangeable/Extendible',
                    'C': 'Redeemable/Exchangeable',
                    'N': 'Perpetual'
                }
            },
            {
                "name": "income",
                "mapping": {
                    'F': 'Fixed Rate Income',
                    'C': 'Cumulative, Fixed Rate Income',
                    'P': 'Participating Income',
                    'Q': 'Cumulative, Participating Income',
                    'A': 'Adjustable/Variable Rate Income',
                    'N': 'Normal Rate Income',
                    'U': 'Auction Rate Income',
                    'D': 'Dividends'
                }
            },
            {
                "name": "form",
                "mapping": {
                    'B': 'Bearer',
                    'R': 'Registered',
                    'N': 'Bearer/Registered',
                    'M': 'Others'
                }
            },
        ],
        ('E', 'L'): [  # Group EL: Limited partnership units
            {
                "name": "voting_right",
                "mapping": {
                    'V': 'Voting',
                    'N': 'Non-Voting',
                    'R': 'Restricted',
                    'E': 'Enhanced voting'
                }
            },
            {
                "name": "ownership",
                "mapping": {
                    'T': 'Restrictions',
                    'U': 'Free'
                }
            },
            {
                "name": "payment_status",
                "mapping": {
                    'F': 'Fully Paid',
                    'O': 'Nil Paid',
                    'P': 'Partly Paid'
                }
            },
            {
                "name": "form",
                "mapping": {
                    'B': 'Bearer',
                    'R': 'Registered',
                    'N': 'Bearer/Registered',
                    'M': 'Others'
                }
            },
        ],
        ('E', 'D'): [  # Group ED: Depositary receipts on equities
            {
                "name": "instrument_dependency",
                "mapping": {
                    'S': 'Common/Ordinary Shares',
                    'P': 'Preferred/Preference Shares',
                    'C': 'Common/Ordinary Convertible Shares',
                    'F': 'Preferred/Preference Convertible Shares',
                    'L': 'Limited Partnership Units',
                    'M': 'Others(Miscellaneous)'
                }
            },
            {
                "name": "underlying_redemption_conversion",
                "mapping": {
                    'R': 'Redeemable',
                    'N': 'Perpetual',
                    'B': 'Convertible',
                    'D': 'Convertible/Redeemable',
                    'X': 'Not Applicable/Undefined'
                }
            },
            {
                "name": "income",
                "mapping": {
                    'F': 'Fixed Rate Income',
                    'C': 'Cumulative, Fixed Rate Income',
                    'P': 'Participating Income',
                    'Q': 'Cumulative, Participating Income',
                    'A': 'Adjustable/Variable Rate Income',
                    'N': 'Normal Rate Income',
                    'U': 'Auction Rate Income',
                    'D': 'Dividends'
                }
            },
            {
                "name": "form",
                "mapping": {
                    'B': 'Bearer',
                    'R': 'Registered',
                    'N': 'Bearer/Registered',
                    'M': 'Others'
                }
            },
        ],
        ('E', 'Y'): [  # Group EY: Structured instruments (participation)
            {
                "name": "type",
                "mapping": {
                    'A': 'Tracker Certificate',
                    'B': 'Outperforming Certificate',
                    'C': 'Bonus Certificate',
                    'D': 'Outperformance Bonus Certificate',
                    'E': 'Twin-Win-Certificate',
                    'M': 'Others'
                }
            },
            {
                "name": "distribution",
                "mapping": {
                    'D': 'Dividend Payments',
                    'Y': 'No Payments',
                    'M': 'Others'
                }
            },
            {
                "name": "repayment",
                "mapping": {
                    'F': 'Cash Repayment',
                    'V': 'Physical Repayment',
                    'E': 'Elect at Settlement',
                    'M': 'Others'
                }
            },
            {
                "name": "underlying_assets",
                "mapping": {
                    'B': 'Baskets',
                    'S': 'Equities',
                    'D': 'Debt Instruments',
                    'G': 'Derivatives',
                    'T': 'Commodities',
                    'C': 'Currencies',
                    'I': 'Indices',
                    'N': 'Interest Rates',
                    'M': 'Others'
                }
            },
        ],
        ('E', 'M'): [  # Group EM: Others
            {
                "name": "na_1",
                "mapping": {
                    'X': 'Not Applicable/Undefined'
                }
            },
            {
                "name": "na_2",
                "mapping": {
                    'X': 'Not Applicable/Undefined'
                }
            },
            {
                "name": "na_3",
                "mapping": {
                    'X': 'Not Applicable/Undefined'
                }
            },
            {
                "name": "form",
                "mapping": {
                    'B': 'Bearer',
                    'R': 'Registered',
                    'N': 'Bearer/Registered',
                    'M': 'Others'
                }
            },
        ],
        
        
        ('C', 'I'): [  # Group CI: Standard (vanilla) investment funds/mutual funds
            {
                "name": "closed_open_end",
                "mapping": {
                    'O': 'Open-End',
                    'C': 'Closed-End',
                    'M': 'Others'
                }
            },
            {
                "name": "distribution_policy",
                "mapping": {
                    'I': 'Income Funds',
                    'G': 'Accumulation Funds',
                    'J': 'Mixed Funds'
                }
            },
            {
                "name": "assets",
                "mapping": {
                    'R': 'Real Estate',
                    'B': 'Debt Instruments',
                    'E': 'Equities',
                    'V': 'Convertible Securities',
                    'L': 'Mixed',
                    'C': 'Commodities',
                    'D': 'Derivatives',
                    'F': 'Referential Instruments',
                    'K': 'Credits',
                    'M': 'Others'
                }
            },
            {
                "name": "security_type_and_restrictions",
                "mapping": {
                    'S': 'Shares',
                    'Q': 'Shares for QI',
                    'U': 'Units',
                    'Y': 'Units for QI'
                }
            },
        ],
        ('C', 'H'): [  # Group CH: Hedge funds
            {
                "name": "investment_strategy",
                "mapping": {
                    'D': 'Directional',
                    'R': 'Relative Value',
                    'S': 'Security Selection',
                    'E': 'Event-Driven',
                    'A': 'Arbitrage',
                    'N': 'Multi-Strategy',
                    'L': 'Asset-Based Lending',
                    'M': 'Others'
                }
            },
            {
                "name": "na_1",
                "mapping": {
                    'X': 'Not Applicable/Undefined'
                }
            },
            {
                "name": "na_2",
                "mapping": {
                    'X': 'Not Applicable/Undefined'
                }
            },
            {
                "name": "na_3",
                "mapping": {
                    'X': 'Not Applicable/Undefined'
                }
            },
        ],
        ('C', 'B'): [  # Group CB: Real estate investment trusts (REITs)
            {
                "name": "closed_open_end",
                "mapping": {
                    'O': 'Open-End',
                    'C': 'Closed-End',
                    'M': 'Others'
                }
            },
            {
                "name": "distribution_policy",
                "mapping": {
                    'I': 'Income Funds',
                    'G': 'Accumulation Funds',
                    'J': 'Mixed Funds'
                }
            },
            {
                "name": "na_1",
                "mapping": {
                    'X': 'Not Applicable/Undefined'
                }
            },
            {
                "name": "security_type_and_restrictions",
                "mapping": {
                    'S': 'Shares',
                    'Q': 'Shares for QI',
                    'U': 'Units',
                    'Y': 'Units for QI'
                }
            },
        ],   
        ('C', 'E'): [  # Group CE: Exchange-traded funds (ETFs)
    {
        "name": "closed_open_end",
        "mapping": {
            'O': 'Open-End',
            'C': 'Closed-End',
            'M': 'Others'
        }
    },
    {
        "name": "distribution_policy",
        "mapping": {
            'I': 'Income Funds',
            'G': 'Accumulation Funds',
            'J': 'Mixed Funds'
        }
    },
    {
        "name": "assets",
        "mapping": {
            'R': 'Real Estate',
            'B': 'Debt Instruments',
            'E': 'Equities',
            'V': 'Convertible Securities',
            'L': 'Mixed',
            'C': 'Commodities',
            'D': 'Derivatives',
            'F': 'Referential Instruments',
            'K': 'Credits',
            'M': 'Others'
        }
    },
    {
        "name": "security_type",
        "mapping": {
            'S': 'Shares',
            'U': 'Units'
        }
    },
],
        ('C', 'S'): [  # Group CS: Pension funds
    {
        "name": "closed_open_end",
        "mapping": {
            'O': 'Open-End',
            'C': 'Closed-End',
            'M': 'Others'
        }
    },
    {
        "name": "strategy_style",
        "mapping": {
            'B': 'Balanced/Conservative',
            'G': 'Growth',
            'L': 'Life Style',
            'M': 'Others'
        }
    },
    {
        "name": "type",
        "mapping": {
            'R': 'Defined Benefit',
            'B': 'Defined Contribution',
            'M': 'Others'
        }
    },
    {
        "name": "security_type",
        "mapping": {
            'S': 'Shares',
            'U': 'Units'
        }
    },
],
        ('C', 'F'): [  # Group CF: Funds of funds
    {
        "name": "closed_open_end",
        "mapping": {
            'O': 'Open-End',
            'C': 'Closed-End',
            'M': 'Others'
        }
    },
    {
        "name": "distribution_policy",
        "mapping": {
            'I': 'Income Funds',
            'G': 'Accumulation Funds',
            'J': 'Mixed Funds'
        }
    },
    {
        "name": "security_type",
        "mapping": {
            'I': 'Standard (Vanilla)',
            'H': 'Hedge Funds',
            'B': 'REIT',
            'E': 'ETF',
            'P': 'Private Equity Funds',
            'M': 'Others'
        }
    },
    {
        "name": "security_type_and_restrictions",
        "mapping": {
            'S': 'Shares',
            'Q': 'Shares for QI',
            'U': 'Units',
            'Y': 'Units for QI'
        }
    },
],
        ('C', 'P'): [  # Group CP: Private equity funds
    {
        "name": "closed_open_end",
        "mapping": {
            'O': 'Open-End',
            'C': 'Closed-End',
            'M': 'Others'
        }
    },
    {
        "name": "distribution_policy",
        "mapping": {
            'I': 'Income Funds',
            'G': 'Accumulation Funds',
            'J': 'Mixed Funds'
        }
    },
    {
        "name": "assets",
        "mapping": {
            'R': 'Real Estate',
            'B': 'Debt Instruments',
            'E': 'Equities',
            'V': 'Convertible Securities',
            'L': 'Mixed',
            'C': 'Commodities',
            'D': 'Derivatives',
            'F': 'Referential Instruments',
            'K': 'Credits',
            'M': 'Others'
        }
    },
    {
        "name": "security_type_and_restrictions",
        "mapping": {
            'S': 'Shares',
            'Q': 'Shares for QI',
            'U': 'Units',
            'Y': 'Units for QI'
        }
    },
],
        ('C', 'M'): [  # Group CM: Others
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_2",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_3",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "security_type_and_restrictions",
        "mapping": {
            'S': 'Shares',
            'Q': 'Shares for QI',
            'U': 'Units',
            'Y': 'Units for QI'
        }
    },
],
    
        ('D', 'B'): [  # Group DB: Bonds
    {
        "name": "interest_type",
        "mapping": {
            'F': 'Fixed Rate',
            'Z': 'Zero Rate/Discounted',
            'V': 'Variable',
            'C': 'Cash Payment',
            'K': 'Payment in Kind'
        }
    },
    {
        "name": "guarantee",
        "mapping": {
            'T': 'Government/State Guarantee',
            'G': 'Joint Guarantee',
            'S': 'Secured',
            'U': 'Unsecured/Unguaranteed',
            'P': 'Negative Pledge',
            'N': 'Senior',
            'O': 'Senior Subordinated',
            'Q': 'Junior',
            'J': 'Junior Subordinated',
            'C': 'Supranational'
        }
    },
    {
        "name": "redemption_reimbursement",
        "mapping": {
            'F': 'Fixed Maturity',
            'G': 'Fixed Maturity with Call Feature',
            'C': 'Fixed Maturity with Put Feature',
            'D': 'Fixed Maturity with Put and Call',
            'A': 'Amortization Plan',
            'B': 'Amortization Plan with Call Feature',
            'T': 'Amortization Plan with Put Feature',
            'L': 'Amortization Plan with Put and Call',
            'P': 'Perpetual',
            'Q': 'Perpetual with Call Feature',
            'R': 'Perpetual with Put Feature',
            'E': 'Extendible'
        }
    },
    {
        "name": "form",
        "mapping": {
            'B': 'Bearer',
            'R': 'Registered',
            'N': 'Bearer/Registered',
            'M': 'Others'
        }
    },
],
        ('D', 'C'): [  # Group DC: Convertible bonds
    {
        "name": "interest_type",
        "mapping": {
            'F': 'Fixed Rate',
            'Z': 'Zero Rate/Discounted',
            'V': 'Variable',
            'K': 'Payment in Kind'
        }
    },
    {
        "name": "guarantee",
        "mapping": {
            'T': 'Government/State Guarantee',
            'G': 'Joint Guarantee',
            'S': 'Secured',
            'U': 'Unsecured/Unguaranteed',
            'P': 'Negative Pledge',
            'N': 'Senior',
            'O': 'Senior Subordinated',
            'Q': 'Junior',
            'J': 'Junior Subordinated',
            'C': 'Supranational'
        }
    },
    {
        "name": "redemption_reimbursement",
        "mapping": {
            'F': 'Fixed Maturity',
            'G': 'Fixed Maturity with Call Feature',
            'C': 'Fixed Maturity with Put Feature',
            'D': 'Fixed Maturity with Put and Call',
            'A': 'Amortization Plan',
            'B': 'Amortization Plan with Call Feature',
            'T': 'Amortization Plan with Put Feature',
            'L': 'Amortization Plan with Put and Call',
            'P': 'Perpetual',
            'Q': 'Perpetual with Call Feature',
            'R': 'Perpetual with Put Feature',
            'E': 'Extendible'
        }
    },
    {
        "name": "form",
        "mapping": {
            'B': 'Bearer',
            'R': 'Registered',
            'N': 'Bearer/Registered',
            'M': 'Others'
        }
    },
],
        ('D', 'W'): [  # Group DW: Bonds with warrants attached
    {
        "name": "interest_type",
        "mapping": {
            'F': 'Fixed Rate',
            'Z': 'Zero Rate/Discounted',
            'V': 'Variable',
            'K': 'Payment in Kind'
        }
    },
    {
        "name": "guarantee",
        "mapping": {
            'T': 'Government/State Guarantee',
            'G': 'Joint Guarantee',
            'S': 'Secured',
            'U': 'Unsecured/Unguaranteed',
            'P': 'Negative Pledge',
            'N': 'Senior',
            'O': 'Senior Subordinated',
            'Q': 'Junior',
            'J': 'Junior Subordinated',
            'C': 'Supranational'
        }
    },
    {
        "name": "redemption_reimbursement",
        "mapping": {
            'F': 'Fixed Maturity',
            'G': 'Fixed Maturity with Call Feature',
            'C': 'Fixed Maturity with Put Feature',
            'D': 'Fixed Maturity with Put and Call',
            'A': 'Amortization Plan',
            'B': 'Amortization Plan with Call Feature',
            'T': 'Amortization Plan with Put Feature',
            'L': 'Amortization Plan with Put and Call',
            'P': 'Perpetual',
            'Q': 'Perpetual with Call Feature',
            'R': 'Perpetual with Put Feature',
            'E': 'Extendible'
        }
    },
    {
        "name": "form",
        "mapping": {
            'B': 'Bearer',
            'R': 'Registered',
            'N': 'Bearer/Registered',
            'M': 'Others'
        }
    },
],
        ('D', 'T'): [  # Group DT: Medium term notes
    {
        "name": "interest_type",
        "mapping": {
            'F': 'Fixed Rate',
            'Z': 'Zero Rate/Discounted',
            'V': 'Variable',
            'K': 'Payment in Kind'
        }
    },
    {
        "name": "guarantee",
        "mapping": {
            'T': 'Government/State Guarantee',
            'G': 'Joint Guarantee',
            'S': 'Secured',
            'U': 'Unsecured/Unguaranteed',
            'P': 'Negative Pledge',
            'N': 'Senior',
            'O': 'Senior Subordinated',
            'Q': 'Junior',
            'J': 'Junior Subordinated',
            'C': 'Supranational'
        }
    },
    {
        "name": "redemption_reimbursement",
        "mapping": {
            'F': 'Fixed Maturity',
            'G': 'Fixed Maturity with Call Feature',
            'C': 'Fixed Maturity with Put Feature',
            'D': 'Fixed Maturity with Put and Call',
            'A': 'Amortization Plan',
            'B': 'Amortization Plan with Call Feature',
            'T': 'Amortization Plan with Put Feature',
            'L': 'Amortization Plan with Put and Call',
            'P': 'Perpetual',
            'Q': 'Perpetual with Call Feature',
            'R': 'Perpetual with Put Feature',
            'E': 'Extendible'
        }
    },
    {
        "name": "form",
        "mapping": {
            'B': 'Bearer',
            'R': 'Registered',
            'N': 'Bearer/Registered',
            'M': 'Others'
        }
    },
],
        ('D', 'S'): [  # Group DS: Structured products (capital protection)
    {
        "name": "type",
        "mapping": {
            'A': 'Capital Protection Certificate with Participation',
            'B': 'Capital Protection Convertible Certificate',
            'C': 'Barrier Capital Protection Certificate',
            'D': 'Capital Protection Certificate with Coupons',
            'M': 'Others'
        }
    },
    {
        "name": "distribution",
        "mapping": {
            'F': 'Fixed Interest Payments',
            'D': 'Dividend Payments',
            'V': 'Variable Interest Payments',
            'Y': 'No Payments',
            'M': 'Others(Miscellaneous)'
        }
    },
    {
        "name": "repayment",
        "mapping": {
            'F': 'Fixed Cash Repayment (Only Protected Capital Level)',
            'V': 'Variable Cash Repayment',
            'M': 'Others(Miscellaneous)'
        }
    },
    {
        "name": "underlying_assets",
        "mapping": {
            'B': 'Baskets',
            'S': 'Equities',
            'D': 'Debt Instruments',
            'T': 'Commodities',
            'C': 'Currencies (Specified Exchange Rate)',
            'I': 'Indices (The Performance of an Index)',
            'N': 'Interest Rates',
            'M': 'Others'
        }
    },
],
        ('D', 'E'): [  # Group DE: Structured products (without capital protection)
    {
        "name": "type",
        "mapping": {
            'A': 'Discount Certificate',
            'B': 'Barrier Discount Certificate',
            'C': 'Reverse Convertible',
            'D': 'Barrier Reverse Convertible',
            'E': 'Express Certificate',
            'M': 'Others'
        }
    },
    {
        "name": "distribution",
        "mapping": {
            'F': 'Fixed Interest Payments',
            'D': 'Dividend Payments',
            'V': 'Variable Interest Payments',
            'Y': 'No Payments',
            'M': 'Others(Miscellaneous)'
        }
    },
    {
        "name": "repayment",
        "mapping": {
            'R': 'Repayment in Cash',
            'S': 'Repayment in Assets',
            'C': 'Repayment in Assets and Cash',
            'T': 'Repayment in Assets or Cash',
            'M': 'Others'
        }
    },
    {
        "name": "underlying_assets",
        "mapping": {
            'B': 'Baskets',
            'S': 'Equities',
            'D': 'Debt Instruments',
            'T': 'Commodities',
            'C': 'Currencies (Specified Exchange Rate)',
            'I': 'Indices (The Performance of an Index)',
            'N': 'Interest Rates',
            'M': 'Others'
        }
    },
],
        ('D', 'G'): [  # Group DG: Mortgage-backed securities
    {
        "name": "interest_type",
        "mapping": {
            'F': 'Fixed Rate',
            'Z': 'Zero Rate/Discounted',
            'V': 'Variable'
        }
    },
    {
        "name": "guarantee",
        "mapping": {
            'T': 'Government/State Guarantee',
            'G': 'Joint Guarantee',
            'S': 'Secured',
            'U': 'Unsecured/Unguaranteed',
            'P': 'Negative Pledge',
            'N': 'Senior',
            'O': 'Senior Subordinated',
            'Q': 'Junior',
            'J': 'Junior Subordinated',
            'C': 'Supranational'
        }
    },
    {
        "name": "redemption_reimbursement",
        "mapping": {
            'F': 'Fixed Maturity',
            'G': 'Fixed Maturity with Call Feature',
            'C': 'Fixed Maturity with Put Feature',
            'D': 'Fixed Maturity with Put and Call',
            'A': 'Amortization Plan',
            'B': 'Amortization Plan with Call Feature',
            'T': 'Amortization Plan with Put Feature',
            'L': 'Amortization Plan with Put and Call',
            'P': 'Perpetual',
            'Q': 'Perpetual with Call Feature',
            'R': 'Perpetual with Put Feature',
            'E': 'Extendible'
        }
    },
    {
        "name": "form",
        "mapping": {
            'B': 'Bearer',
            'R': 'Registered',
            'N': 'Bearer/Registered',
            'M': 'Others'
        }
    },
],
        ('D', 'A'): [  # Group DA: Asset-backed securities
    {
        "name": "interest_type",
        "mapping": {
            'F': 'Fixed Rate',
            'Z': 'Zero Rate/Discounted',
            'V': 'Variable'
        }
    },
    {
        "name": "guarantee",
        "mapping": {
            'T': 'Government/State Guarantee',
            'G': 'Joint Guarantee',
            'S': 'Secured',
            'U': 'Unsecured/Unguaranteed',
            'P': 'Negative Pledge',
            'N': 'Senior',
            'O': 'Senior Subordinated',
            'Q': 'Junior',
            'J': 'Junior Subordinated',
            'C': 'Supranational'
        }
    },
    {
        "name": "redemption_reimbursement",
        "mapping": {
            'F': 'Fixed Maturity',
            'G': 'Fixed Maturity with Call Feature',
            'C': 'Fixed Maturity with Put Feature',
            'D': 'Fixed Maturity with Put and Call',
            'A': 'Amortization Plan',
            'B': 'Amortization Plan with Call Feature',
            'T': 'Amortization Plan with Put Feature',
            'L': 'Amortization Plan with Put and Call',
            'P': 'Perpetual',
            'Q': 'Perpetual with Call Feature',
            'R': 'Perpetual with Put Feature',
            'E': 'Extendible'
        }
    },
    {
        "name": "form",
        "mapping": {
            'B': 'Bearer',
            'R': 'Registered',
            'N': 'Bearer/Registered',
            'M': 'Others'
        }
    },
],
        ('D', 'N'): [  # Group DN: Municipal bonds
    {
        "name": "interest_type",
        "mapping": {
            'F': 'Fixed Rate',
            'Z': 'Zero Rate/Discounted',
            'V': 'Variable'
        }
    },
    {
        "name": "guarantee",
        "mapping": {
            'T': 'Government/State Guarantee',
            'G': 'Joint Guarantee',
            'S': 'Secured',
            'U': 'Unsecured/Unguaranteed',
            'P': 'Negative Pledge',
            'N': 'Senior',
            'O': 'Senior Subordinated',
            'Q': 'Junior',
            'J': 'Junior Subordinated',
            'C': 'Supranational'
        }
    },
    {
        "name": "redemption_reimbursement",
        "mapping": {
            'F': 'Fixed Maturity',
            'G': 'Fixed Maturity with Call Feature',
            'C': 'Fixed Maturity with Put Feature',
            'D': 'Fixed Maturity with Put and Call',
            'A': 'Amortization Plan',
            'B': 'Amortization Plan with Call Feature',
            'T': 'Amortization Plan with Put Feature',
            'L': 'Amortization Plan with Put and Call',
            'P': 'Perpetual',
            'Q': 'Perpetual with Call Feature',
            'R': 'Perpetual with Put Feature',
            'E': 'Extendible'
        }
    },
    {
        "name": "form",
        "mapping": {
            'B': 'Bearer',
            'R': 'Registered',
            'N': 'Bearer/Registered',
            'M': 'Others'
        }
    },
],
        ('D', 'D'): [  # Group DD: Depositary receipts on debt instruments
    {
        "name": "instrument_dependency",
        "mapping": {
            'B': 'Bonds',
            'C': 'Convertible Bonds',
            'W': 'Bonds with Warrants Attached',
            'T': 'Medium-Term Notes',
            'Y': 'Money Market Instruments',
            'G': 'Mortgage-Backed Securities',
            'Q': 'Asset-Backed Securities',
            'N': 'Municipal Bonds',
            'M': 'Others'
        }
    },
    {
        "name": "interest_or_cash_payment",
        "mapping": {
            'F': 'Fixed Rate',
            'Z': 'Zero Rate/Discounted',
            'V': 'Variable',
            'C': 'Cash Payment'
        }
    },
    {
        "name": "guarantee",
        "mapping": {
            'T': 'Government/State Guarantee',
            'G': 'Joint Guarantee',
            'S': 'Secured',
            'U': 'Unsecured/Unguaranteed',
            'P': 'Negative Pledge',
            'N': 'Senior',
            'O': 'Senior Subordinated',
            'Q': 'Junior',
            'J': 'Junior Subordinated',
            'C': 'Supranational'
        }
    },
    {
        "name": "redemption_reimbursement",
        "mapping": {
            'F': 'Fixed Maturity',
            'G': 'Fixed Maturity with Call Feature',
            'C': 'Fixed Maturity with Put Feature',
            'D': 'Fixed Maturity with Put and Call',
            'A': 'Amortization Plan',
            'B': 'Amortization Plan with Call Feature',
            'T': 'Amortization Plan with Put Feature',
            'L': 'Amortization Plan with Put and Call',
            'P': 'Perpetual',
            'Q': 'Perpetual with Call Feature',
            'R': 'Perpetual with Put Feature',
            'E': 'Extendible'
        }
    },
],
        ('D', 'M'): [  # Group DM: Other
    {
        "name": "type",
        "mapping": {
            'B': 'Bank Loan',
            'P': 'Promissory Note',
            'M': 'Others'
        }
    },
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_2",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "form",
        "mapping": {
            'B': 'Bearer',
            'R': 'Registered',
            'N': 'Bearer/Registered',
            'M': 'Others'
        }
    },
],
        ('D', 'Y'): [  # Group DY: Money Market Instruments
    {
        "name": "interest_type",
        "mapping": {
            'F': 'Fixed Rate',
            'Z': 'Zero Rate/Discounted',
            'V': 'Variable',
            'K': 'Payment in Kind'
        }
    },
    {
        "name": "guarantee",
        "mapping": {
            'T': 'Government/State Guarantee',
            'G': 'Joint Guarantee',
            'S': 'Secured',
            'U': 'Unsecured/Unguaranteed',
            'P': 'Negative Pledge',
            'N': 'Senior',
            'O': 'Senior Subordinated',
            'Q': 'Junior',
            'J': 'Junior Subordinated',
            'C': 'Supranational'
        }
    },
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "form",
        "mapping": {
            'B': 'Bearer',
            'R': 'Registered',
            'N': 'Bearer/Registered',
            'M': 'Others'
        }
    },
],
    
        ('R', 'A'): [  # Group RA: Allotments (Bonus Rights)
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_2",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_3",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "form",
        "mapping": {
            'B': 'Bearer',
            'R': 'Registered',
            'N': 'Bearer/Registered',
            'M': 'Others'
        }
    },
],
        ('R', 'S'): [  # Group RS: Subscription Rights
    {
        "name": "assets",
        "mapping": {
            'S': 'Common/Ordinary Shares',
            'P': 'Preferred/Preference Shares',
            'C': 'Common/Ordinary Convertible Shares',
            'F': 'Preferred/Preference Convertible Shares',
            'B': 'Bonds',
            'I': 'Combined Instruments',
            'M': 'Others'
        }
    },
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_2",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "form",
        "mapping": {
            'B': 'Bearer',
            'R': 'Registered',
            'N': 'Bearer/Registered',
            'M': 'Others'
        }
    },
],
        ('R', 'P'): [  # Group RP: Purchase Rights
    {
        "name": "assets",
        "mapping": {
            'S': 'Common/Ordinary Shares',
            'P': 'Preferred/Preference Shares',
            'C': 'Common/Ordinary Convertible Shares',
            'F': 'Preferred/Preference Convertible Shares',
            'B': 'Bonds',
            'I': 'Combined Instruments',
            'M': 'Others'
        }
    },
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_2",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "form",
        "mapping": {
            'B': 'Bearer',
            'R': 'Registered',
            'N': 'Bearer/Registered',
            'M': 'Others'
        }
    },
],
        ('R', 'W'): [  # Group RW: Warrants
    {
        "name": "underlying_assets",
        "mapping": {
            'B': 'Baskets',
            'S': 'Equities',
            'D': 'Debt Instruments/Interest Rates',
            'T': 'Commodities',
            'C': 'Currencies',
            'I': 'Indices',
            'M': 'Others'
        }
    },
    {
        "name": "type",
        "mapping": {
            'T': 'Traditional Warrants',
            'N': 'Naked Warrants',
            'C': 'Covered Warrants'
        }
    },
    {
        "name": "call_put",
        "mapping": {
            'C': 'Call',
            'P': 'Put',
            'B': 'Call and Put'
        }
    },
    {
        "name": "exercise_option_style",
        "mapping": {
            'A': 'American',
            'E': 'European',
            'B': 'Bermudan',
            'M': 'Others'
        }
    },
],
        ('R', 'F'): [  # Group RF: Mini-future certificates / constant leverage certificates
    {
        "name": "underlying_assets",
        "mapping": {
            'B': 'Baskets',
            'S': 'Equities',
            'D': 'Debt Instruments/Interest Rates',
            'T': 'Commodities',
            'C': 'Currencies',
            'I': 'Indices',
            'M': 'Others'
        }
    },
    {
        "name": "barrier_dependency_type",
        "mapping": {
            'T': 'Barrier Underlying Based',
            'N': 'Barrier Instrument Based',
            'M': 'Others(Miscellaneous)'
        }
    },
    {
        "name": "long_short",
        "mapping": {
            'C': 'Long',
            'P': 'Short',
            'M': 'Others(Miscellaneous)'
        }
    },
    {
        "name": "exercise_option_style",
        "mapping": {
            'A': 'American',
            'E': 'European',
            'B': 'Bermudan',
            'M': 'Others'
        }
    },
],
        ('R', 'D'): [  # Group RD: Depositary receipts on entitlements
    {
        "name": "instrument_dependency",
        "mapping": {
            'A': 'Allotment (Bonus) Rights',
            'S': 'Subscription Rights',
            'P': 'Purchase Rights',
            'W': 'Warrants',
            'M': 'Others'
        }
    },
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_2",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "form",
        "mapping": {
            'B': 'Bearer',
            'R': 'Registered',
            'N': 'Bearer/Registered',
            'M': 'Others'
        }
    },
],
        ('R', 'M'): [  # Group RM: Other
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_2",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_3",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_4",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
],
    
        ('O', 'C'): [  # Group OC: Call options
    {
        "name": "exercise_option_style",
        "mapping": {
            'A': 'American',
            'E': 'European',
            'B': 'Bermudan'
        }
    },
    {
        "name": "underlying_assets",
        "mapping": {
            'B': 'Baskets',
            'S': 'Stock-Equities',
            'D': 'Debt Instruments',
            'T': 'Commodities',
            'C': 'Currencies',
            'I': 'Indices',
            'O': 'Options',
            'F': 'Futures',
            'W': 'Swaps',
            'N': 'Interest Rates',
            'M': 'Others'
        }
    },
    {
        "name": "delivery",
        "mapping": {
            'P': 'Physical',
            'C': 'Cash',
            'N': 'Non-Deliverable',
            'E': 'Elect at Exercise'
        }
    },
    {
        "name": "standardization",
        "mapping": {
            'S': 'Standardized',
            'N': 'Non-Standardized'
        }
    },
],
        ('O', 'P'): [  # Group OP: Put options
    {
        "name": "exercise_option_style",
        "mapping": {
            'A': 'American',
            'E': 'European',
            'B': 'Bermudan'
        }
    },
    {
        "name": "underlying_assets",
        "mapping": {
            'B': 'Baskets',
            'S': 'Stock-Equities',
            'D': 'Debt Instruments',
            'T': 'Commodities',
            'C': 'Currencies',
            'I': 'Indices',
            'O': 'Options',
            'F': 'Futures',
            'W': 'Swaps',
            'N': 'Interest Rates',
            'M': 'Others'
        }
    },
    {
        "name": "delivery",
        "mapping": {
            'P': 'Physical',
            'C': 'Cash',
            'N': 'Non-Deliverable',
            'E': 'Elect at Exercise'
        }
    },
    {
        "name": "standardization",
        "mapping": {
            'S': 'Standardized',
            'N': 'Non-Standardized'
        }
    },
],
        ('O', 'M'): [  # Group OM: Other
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_2",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_3",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_4",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
],
    
        ('F', 'F'): [  # Group FF: Financial futures
    {
        "name": "underlying_assets",
        "mapping": {
            'B': 'Baskets',
            'S': 'Stock-Equities',
            'D': 'Debt Instruments',
            'C': 'Currencies',
            'I': 'Indices',
            'O': 'Options',
            'F': 'Futures',
            'W': 'Swaps',
            'N': 'Interest Rates',
            'V': 'Stock Dividend',
            'M': 'Others'
        }
    },
    {
        "name": "delivery",
        "mapping": {
            'P': 'Physical',
            'C': 'Cash',
            'N': 'Non-Deliverable'
        }
    },
    {
        "name": "standardization",
        "mapping": {
            'S': 'Standardized',
            'N': 'Non-Standardized'
        }
    },
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
],
        ('F', 'C'): [  # Group FC: Commodities futures
    {
        "name": "underlying_assets",
        "mapping": {
            'E': 'Extraction Resources',
            'A': 'Agriculture',
            'I': 'Industrial Products',
            'S': 'Services',
            'N': 'Environmental',
            'P': 'Polypropylene Products',
            'H': 'Generated Resources',
            'M': 'Others'
        }
    },
    {
        "name": "delivery",
        "mapping": {
            'P': 'Physical',
            'C': 'Cash',
            'N': 'Non-Deliverable'
        }
    },
    {
        "name": "standardization",
        "mapping": {
            'S': 'Standardized',
            'N': 'Non-Standardized'
        }
    },
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
],
    
        ('S', 'R'): [  # Group SR: Rates
    {
        "name": "underlying_assets",
        "mapping": {
            'A': 'Basis swap',
            'C': 'Fixed-Floating',
            'D': 'Fixed-Fixed',
            'G': 'Inflation rate index',
            'H': 'Overnight Index Swap (OIS)',
            'Z': 'Zero coupon',
            'M': 'Others'
        }
    },
    {
        "name": "notional",
        "mapping": {
            'C': 'Constant',
            'D': 'Accreting',
            'I': 'Amortizing',
            'Y': 'Custom'
        }
    },
    {
        "name": "currency_structure",
        "mapping": {
            'S': 'Single-Currency',
            'C': 'Cross-Currency'
        }
    },
    {
        "name": "delivery",
        "mapping": {
            'C': 'Cash',
            'P': 'Physical'
        }
    },
],
        ('S', 'T'): [  # Group ST: Commodities
    {
        "name": "underlying_assets",
        "mapping": {
            'J': 'Energy',
            'K': 'Metals',
            'A': 'Agriculture',
            'N': 'Environmental',
            'G': 'Freight',
            'P': 'Polypropylene Products',
            'S': 'Fertilizer',
            'T': 'Paper',
            'I': 'Index',
            'Q': 'Multi-Commodity',
            'M': 'Others'
        }
    },
    {
        "name": "return_or_payout_trigger",
        "mapping": {
            'P': 'Price',
            'D': 'Dividend',
            'V': 'Variance',
            'L': 'Volatility',
            'T': 'Total return',
            'C': 'Contract for difference',
            'M': 'Others'
        }
    },
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "delivery",
        "mapping": {
            'C': 'Cash',
            'P': 'Physical',
            'E': 'Elect at settlement'
        }
    },
],
        ('S', 'E'): [  # Group SE: Equity
    {
        "name": "underlying_assets",
        "mapping": {
            'S': 'Single stock',
            'I': 'Index',
            'B': 'Basket',
            'M': 'Others'
        }
    },
    {
        "name": "return_or_payout_trigger",
        "mapping": {
            'P': 'Price',
            'D': 'Dividend',
            'V': 'Variance',
            'L': 'Volatility',
            'T': 'Total return',
            'C': 'Contract for difference',
            'M': 'Others'
        }
    },
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "delivery",
        "mapping": {
            'C': 'Cash',
            'P': 'Physical',
            'E': 'Elect at settlement'
        }
    },
],
        ('S', 'C'): [  # Group SC: Credit
    {
        "name": "underlying_assets",
        "mapping": {
            'U': 'Single name',
            'V': 'Index tranche',
            'I': 'Index',
            'B': 'Basket',
            'M': 'Others'
        }
    },
    {
        "name": "return_or_payout_trigger",
        "mapping": {
            'C': 'Credit default',
            'T': 'Total return',
            'M': 'Others'
        }
    },
    {
        "name": "underlying_issuer_type",
        "mapping": {
            'C': 'Corporate',
            'S': 'Sovereign',
            'L': 'Local'
        }
    },
    {
        "name": "delivery",
        "mapping": {
            'C': 'Cash',
            'P': 'Physical',
            'A': 'Auction'
        }
    },
],
        ('S', 'F'): [  # Group SF: Foreign exchange
    {
        "name": "underlying_assets",
        "mapping": {
            'A': 'Spot-Forward swap',
            'C': 'Forward-forward swap',
            'M': 'Others'
        }
    },
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_2",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "delivery",
        "mapping": {
            'P': 'Physical',
            'N': 'Non-Deliverable'
        }
    },
],
        ('S', 'M'): [  # Group SM: Other
    {
        "name": "underlying_assets",
        "mapping": {
            'P': 'Commercial property (or property derivative)',
            'M': 'Others'
        }
    },
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_2",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "delivery",
        "mapping": {
            'C': 'Cash',
            'P': 'Physical'
        }
    },
],
    
        ('H', 'R'): [  # Group HR: Rates
    {
        "name": "underlying_assets",
        "mapping": {
            'A': 'Basis swap',
            'C': 'Fixed-Floating',
            'D': 'Fixed-Fixed',
            'G': 'Inflation rate index',
            'H': 'Overnight Index Swap (OIS)',
            'O': 'Options',
            'R': 'Forwards',
            'F': 'Futures',
            'M': 'Others'
        }
    },
    {
        "name": "option_style_and_type",
        "mapping": {
            'A': 'European Call',
            'B': 'American Call',
            'C': 'Bermudan Call',
            'D': 'European Put',
            'E': 'American Put',
            'F': 'Bermudan Put',
            'G': 'European Chooser',
            'H': 'American Chooser',
            'I': 'Bermudan Chooser'
        }
    },
    {
        "name": "valuation_method_or_trigger",
        "mapping": {
            'V': 'Vanilla',
            'A': 'Asian',
            'D': 'Digital (Binary)',
            'B': 'Barrier',
            'G': 'Digital barrier',
            'L': 'Lookback',
            'P': 'Other path dependent',
            'M': 'Others'
        }
    },
    {
        "name": "delivery",
        "mapping": {
            'C': 'Cash',
            'P': 'Physical',
            'E': 'Elect at Exercise'
        }
    },
],
        ('H', 'T'): [  # Group HT: Commodities
    {
        "name": "underlying_assets",
        "mapping": {
            'J': 'Energy',
            'K': 'Metals',
            'A': 'Agriculture',
            'N': 'Environmental',
            'G': 'Freight',
            'P': 'Polypropylene Products',
            'S': 'Fertilizer',
            'T': 'Paper',
            'I': 'Index',
            'Q': 'Multi-Commodity',
            'O': 'Options',
            'R': 'Forwards',
            'F': 'Futures',
            'W': 'Swaps',
            'M': 'Others'
        }
    },
    {
        "name": "option_style_and_type",
        "mapping": {
            'A': 'European Call',
            'B': 'American Call',
            'C': 'Bermudan Call',
            'D': 'European Put',
            'E': 'American Put',
            'F': 'Bermudan Put',
            'G': 'European Chooser',
            'H': 'American Chooser',
            'I': 'Bermudan Chooser'
        }
    },
    {
        "name": "valuation_method_or_trigger",
        "mapping": {
            'V': 'Vanilla',
            'A': 'Asian',
            'D': 'Digital (Binary)',
            'B': 'Barrier',
            'G': 'Digital barrier',
            'L': 'Lookback',
            'P': 'Other path dependent',
            'M': 'Others'
        }
    },
    {
        "name": "delivery",
        "mapping": {
            'C': 'Cash',
            'P': 'Physical',
            'E': 'Elect at Exercise'
        }
    },
],
        ('H', 'E'): [  # Group HE: Equity
    {
        "name": "underlying_assets",
        "mapping": {
            'S': 'Single stock',
            'I': 'Index',
            'B': 'Basket',
            'O': 'Options',
            'R': 'Forwards',
            'F': 'Futures',
            'M': 'Others'
        }
    },
    {
        "name": "option_style_and_type",
        "mapping": {
            'A': 'European Call',
            'B': 'American Call',
            'C': 'Bermudan Call',
            'D': 'European Put',
            'E': 'American Put',
            'F': 'Bermudan Put',
            'G': 'European Chooser',
            'H': 'American Chooser',
            'I': 'Bermudan Chooser'
        }
    },
    {
        "name": "valuation_method_or_trigger",
        "mapping": {
            'V': 'Vanilla',
            'A': 'Asian',
            'D': 'Digital (Binary)',
            'B': 'Barrier',
            'G': 'Digital barrier',
            'L': 'Lookback',
            'P': 'Other path dependent',
            'M': 'Others'
        }
    },
    {
        "name": "delivery",
        "mapping": {
            'C': 'Cash',
            'P': 'Physical',
            'E': 'Elect at Exercise'
        }
    },
],
        ('H', 'C'): [  # Group HC: Credit
    {
        "name": "underlying_assets",
        "mapping": {
            'U': 'CDS on a single name',
            'V': 'CDS on an index tranche',
            'I': 'CDS on an index',
            'W': 'Swaps',
            'M': 'Others'
        }
    },
    {
        "name": "option_style_and_type",
        "mapping": {
            'A': 'European Call',
            'B': 'American Call',
            'C': 'Bermudan Call',
            'D': 'European Put',
            'E': 'American Put',
            'F': 'Bermudan Put',
            'G': 'European Chooser',
            'H': 'American Chooser',
            'I': 'Bermudan Chooser'
        }
    },
    {
        "name": "valuation_method_or_trigger",
        "mapping": {
            'V': 'Vanilla',
            'A': 'Asian',
            'D': 'Digital (Binary)',
            'B': 'Barrier',
            'G': 'Digital barrier',
            'L': 'Lookback',
            'P': 'Other path dependent',
            'M': 'Others'
        }
    },
    {
        "name": "delivery",
        "mapping": {
            'C': 'Cash',
            'P': 'Physical',
            'E': 'Elect at Exercise'
        }
    },
],
        ('H', 'F'): [  # Group HF: Foreign exchange
    {
        "name": "underlying_assets",
        "mapping": {
            'R': 'Forwards',
            'F': 'Futures',
            'T': 'Spot-Forward swap',
            'V': 'Volatility',
            'M': 'Others'
        }
    },
    {
        "name": "option_style_and_type",
        "mapping": {
            'A': 'European Call',
            'B': 'American Call',
            'C': 'Bermudan Call',
            'D': 'European Put',
            'E': 'American Put',
            'F': 'Bermudan Put',
            'G': 'European Chooser',
            'H': 'American Chooser',
            'I': 'Bermudan Chooser'
        }
    },
    {
        "name": "valuation_method_or_trigger",
        "mapping": {
            'V': 'Vanilla',
            'A': 'Asian',
            'D': 'Digital (Binary)',
            'B': 'Barrier',
            'G': 'Digital barrier',
            'L': 'Lookback',
            'P': 'Other path dependent',
            'M': 'Others'
        }
    },
    {
        "name": "delivery",
        "mapping": {
            'C': 'Cash',
            'P': 'Physical',
            'E': 'Elect at Exercise',
            'N': 'Non-Deliverable'
        }
    },
],
        ('H', 'M'): [  # Group HM: Other
    {
        "name": "underlying_assets",
        "mapping": {
            'P': 'Commercial property (or property derivative)',
            'M': 'Others'
        }
    },
    {
        "name": "option_style_and_type",
        "mapping": {
            'A': 'European Call',
            'B': 'American Call',
            'C': 'Bermudan Call',
            'D': 'European Put',
            'E': 'American Put',
            'F': 'Bermudan Put',
            'G': 'European Chooser',
            'H': 'American Chooser',
            'I': 'Bermudan Chooser'
        }
    },
    {
        "name": "valuation_method_or_trigger",
        "mapping": {
            'V': 'Vanilla',
            'A': 'Asian',
            'D': 'Digital (Binary)',
            'B': 'Barrier',
            'G': 'Digital barrier',
            'L': 'Lookback',
            'P': 'Other path dependent',
            'M': 'Others'
        }
    },
    {
        "name": "delivery",
        "mapping": {
            'C': 'Cash',
            'P': 'Physical',
            'E': 'Elect at Exercise',
            'N': 'Non-Deliverable',
            'A': 'Auction'
        }
    },
],
    
        ('I', 'F'): [  # Group IF: Foreign exchange
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_2",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_3",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "delivery",
        "mapping": {
            'P': 'Physical'
        }
    },
],
        ('I', 'T'): [  # Group IT: Commodities
    {
        "name": "underlying_assets",
        "mapping": {
            'A': 'Agriculture',
            'J': 'Energy',
            'K': 'Metals',
            'N': 'Environmental',
            'P': 'Polypropylene Products',
            'S': 'Fertilizer',
            'T': 'Paper',
            'M': 'Others'
        }
    },
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_2",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_3",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
],

        ('J', 'E'): [  # Group JE: Equity
    {
        "name": "underlying_assets",
        "mapping": {
            'S': 'Single stock',
            'I': 'Index',
            'B': 'Basket',
            'O': 'Options',
            'F': 'Futures'
        }
    },
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "return_or_payout_trigger",
        "mapping": {
            'C': 'Contract for difference',
            'S': 'Spread-bet',
            'F': 'Forward price of underlying instrument'
        }
    },
    {
        "name": "delivery",
        "mapping": {
            'C': 'Cash',
            'P': 'Physical'
        }
    },
],
        ('J', 'F'): [  # Group JF: Foreign exchange
    {
        "name": "underlying_assets",
        "mapping": {
            'T': 'Spot',
            'R': 'Forward',
            'O': 'Options',
            'F': 'Futures'
        }
    },
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "return_or_payout_trigger",
        "mapping": {
            'C': 'Contract for difference',
            'S': 'Spread-bet',
            'F': 'Forward price of underlying instrument'
        }
    },
    {
        "name": "delivery",
        "mapping": {
            'P': 'Physical',
            'C': 'Cash',
            'N': 'Non-Deliverable'
        }
    },
],
        ('J', 'C'): [  # Group JC: Credit
    {
        "name": "underlying_assets",
        "mapping": {
            'A': 'Single name',
            'I': 'Index',
            'B': 'Basket',
            'C': 'CDS on a single name',
            'D': 'CDS on an index',
            'G': 'CDS on a basket',
            'O': 'Options'
        }
    },
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "return_or_payout_trigger",
        "mapping": {
            'S': 'Spread-bet',
            'F': 'Forward price of underlying instrument'
        }
    },
    {
        "name": "delivery",
        "mapping": {
            'P': 'Physical',
            'C': 'Cash',
            'N': 'Non-Deliverable'
        }
    },
],
        ('J', 'R'): [  # Group JR: Rates
    {
        "name": "underlying_assets",
        "mapping": {
            'I': 'Interest rate index',
            'O': 'Options',
            'M': 'Others'
        }
    },
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "return_or_payout_trigger",
        "mapping": {
            'S': 'Spread-bet',
            'F': 'Forward price of underlying instrument'
        }
    },
    {
        "name": "delivery",
        "mapping": {
            'P': 'Physical',
            'C': 'Cash',
            'N': 'Non-Deliverable'
        }
    },
],
        ('J', 'T'): [  # Group JT: Commodities
    {
        "name": "underlying_assets",
        "mapping": {
            'A': 'Agriculture',
            'B': 'Basket',
            'G': 'Freight',
            'I': 'Index',
            'J': 'Energy',
            'K': 'Metals',
            'N': 'Environmental',
            'P': 'Polypropylene Products',
            'S': 'Fertilizer',
            'T': 'Paper',
            'M': 'Others'
        }
    },
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "return_or_payout_trigger",
        "mapping": {
            'C': 'Contract for difference',
            'F': 'Forward price of underlying instrument'
        }
    },
    {
        "name": "delivery",
        "mapping": {
            'P': 'Physical',
            'C': 'Cash',
            'N': 'Non-Deliverable'
        }
    },
],
    
        ('K', 'R'): [  # Group KR: Rates
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_2",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_3",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_4",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
],
        ('K', 'T'): [  # Group KT: Commodities
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_2",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_3",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_4",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
],
        ('K', 'E'): [  # Group KE: Equity
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_2",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_3",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_4",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
],
        ('K', 'C'): [  # Group KC: Credit
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_2",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_3",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_4",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
],
        ('K', 'F'): [  # Group KF: Foreign exchange
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_2",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_3",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_4",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
],
        ('K', 'Y'): [  # Group KY: Mixed assets
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_2",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_3",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_4",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
],
        ('K', 'M'): [  # Group KM: Other
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_2",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_3",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_4",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
],

        ('L', 'L'): [  # Group LL: Loan-lease
    {
        "name": "underlying_assets",
        "mapping": {
            'A': 'Agriculture',
            'B': 'Baskets',
            'J': 'Energy',
            'K': 'Metals',
            'N': 'Environmental',
            'P': 'Polypropylene Products',
            'S': 'Fertilizer',
            'T': 'Paper',
            'M': 'Others'
        }
    },
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_2",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "delivery",
        "mapping": {
            'P': 'Physical',
            'C': 'Cash',
            'N': 'Non-Deliverable'
        }
    },
],
        ('L', 'R'): [  # Group LR: Repurchase agreements
    {
        "name": "underlying_assets",
        "mapping": {
            'G': 'General collateral',
            'S': 'Specific security collateral',
            'C': 'Cash collateral'
        }
    },
    {
        "name": "termination_type",
        "mapping": {
            'F': 'Flexible',
            'N': 'Overnight',
            'O': 'Open',
            'T': 'Term'
        }
    },
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "delivery",
        "mapping": {
            'D': 'Delivery versus payment',
            'H': 'Hold-in-custody',
            'T': 'Tri-party'
        }
    },
],
        ('L', 'S'): [  # Group LS: Securities lending
    {
        "name": "underlying_assets",
        "mapping": {
            'C': 'Cash collateral',
            'G': 'Government bonds',
            'P': 'Corporate bonds',
            'T': 'Convertible bonds',
            'E': 'Equity',
            'L': 'Letter of credit',
            'D': 'Certificate of deposit',
            'W': 'Warrants',
            'K': 'Money Market Instruments',
            'M': 'Others'
        }
    },
    {
        "name": "termination_type",
        "mapping": {
            'N': 'Overnight',
            'O': 'Open',
            'T': 'Term'
        }
    },
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "delivery",
        "mapping": {
            'D': 'Delivery versus payment',
            'F': 'Free of payment',
            'H': 'Hold-in-custody',
            'T': 'Tri-party'
        }
    },
],

        ('T', 'C'): [  # Group TC: Currencies
    {
        "name": "type",
        "mapping": {
            'N': 'National Currency',
            'L': 'Legacy Currency',
            'C': 'Bullion Coins',
            'M': 'Others'
        }
    },
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_2",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_3",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
],
        ('T', 'T'): [  # Group TT: Commodities
    {
        "name": "underlying_assets",
        "mapping": {
            'E': 'Extraction Resources',
            'A': 'Agriculture',
            'I': 'Industrial Products',
            'S': 'Services',
            'N': 'Environmental',
            'P': 'Polypropylene Products',
            'H': 'Generated Resources',
            'M': 'Others'
        }
    },
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_2",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_3",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
],
        ('T', 'R'): [  # Group TR: Interest rates
    {
        "name": "type_of_interest_rates",
        "mapping": {
            'N': 'Nominal',
            'V': 'Variable',
            'F': 'Fixed',
            'R': 'Real',
            'M': 'Others'
        }
    },
    {
        "name": "frequency_of_calculation",
        "mapping": {
            'D': 'Daily',
            'W': 'Weekly',
            'N': 'Monthly',
            'Q': 'Quarterly',
            'S': 'Semi-Annually',
            'A': 'Annually',
            'M': 'Others'
        }
    },
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_2",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
],
        ('T', 'I'): [  # Group TI: Indices
    {
        "name": "asset_classes",
        "mapping": {
            'E': 'Equities',
            'D': 'Debt',
            'F': 'Collective Investment Vehicles',
            'R': 'Real Estate',
            'T': 'Commodities',
            'C': 'Currencies',
            'M': 'Others'
        }
    },
    {
        "name": "weighting_types",
        "mapping": {
            'P': 'Price Weighted',
            'C': 'Capitalization Weighted',
            'E': 'Equal Weighted',
            'F': 'Modified Market Capitalization Weighted',
            'M': 'Others'
        }
    },
    {
        "name": "index_return_types",
        "mapping": {
            'P': 'Price Return',
            'N': 'Net Total Return',
            'G': 'Gross Total Return',
            'M': 'Others'
        }
    },
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
],  
        ('T', 'B'): [  # Group TB: Baskets
    {
        "name": "compositions",
        "mapping": {
            'E': 'Equities',
            'D': 'Debt',
            'F': 'Collective Investment Vehicles',
            'I': 'Indices',
            'T': 'Commodities',
            'C': 'Currencies',
            'M': 'Others'
        }
    },
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_2",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_3",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
],
        ('T', 'D'): [  # Group TD: Stock dividends
    {
        "name": "type_of_equity",
        "mapping": {
            'S': 'Common Ordinary Shares',
            'P': 'Preferred/Preference Shares',
            'C': 'Common Ordinary Convertible Shares',
            'F': 'Preferred/Preference Convertible Shares',
            'L': 'Limited Partnership Units',
            'K': 'Collective Investment Vehicles',
            'M': 'Others'
        }
    },
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_2",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_3",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
],
        ('T', 'M'): [  # Group TM: Others
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_2",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_3",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_4",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
],

        ('M', 'C'): [  # Group MC: Combined instruments
    {
        "name": "components",
        "mapping": {
            'S': 'Combination of Shares',
            'B': 'Combination of Bonds',
            'H': 'Share and Bond',
            'A': 'Share and Warrant',
            'W': 'Warrant and Warrant',
            'U': 'Fund Unit and Other Components',
            'M': 'Others'
        }
    },
    {
        "name": "ownership",
        "mapping": {
            'T': 'Restrictions',
            'U': 'Free'
        }
    },
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "form",
        "mapping": {
            'B': 'Bearer',
            'R': 'Registered',
            'N': 'Bearer/Registered',
            'M': 'Others'
        }
    },
],
        ('M', 'M'): [  # Group MM: Other assets
    {
        "name": "further_grouping",
        "mapping": {
            'R': 'Real Estate Deeds',
            'I': 'Insurance Policies',
            'E': 'Escrow Receipts',
            'T': 'Trade Finance Instruments',
            'N': 'Carbon Credit',
            'P': 'Precious Metal Receipts',
            'S': 'Other OTC Derivative Products',
            'M': 'Others'
        }
    },
    {
        "name": "na_1",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_2",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
    {
        "name": "na_3",
        "mapping": {
            'X': 'Not Applicable/Undefined'
        }
    },
],
    }