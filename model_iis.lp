\ Model mogplex
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  649 x1 + 990 x2 + 941 x3 + 800 x4 + 173 x5 + 138 x6 + 560 x7 + 23 x8
   + 13 x9 + 638 x10 + 303 x11 + 740 x12 + 533 x13 + 671 x14 + 186 x15
   + 152 x16 + 280 x17 + 362 x18 + 590 x19 + 164 x20 + 480 x21 + 368 x22
   + 171 x23 + 651 x24 + 570 x25 + 442 x26 + 228 x27 + 931 x28 + 186 x29
   + 587 x30 + 407 x31 + 826 x32 + 839 x33 + 666 x34 + 964 x35 + 592 x36
   + 923 x37 + 604 x38 + 653 x39 + 164 x40 + 261 x41 + 306 x42 + 481 x43
   + 622 x44 + 365 x45 + 682 x46 + 899 x47 + 842 x48 + 866 x49 + 272 x50
   + 511 x51 + 983 x52 + 921 x53 + 914 x54 + 910 x55 + 282 x56 + 478 x57
   + 472 x58 + 931 x59 + 817 x60 + 972 x61 + 646 x62 + 790 x63 + 971 x64
   + 817 x65 + 543 x66 + 658 x67 + 52 x68 + 76 x69 + 454 x70 + 195 x71
   + 652 x72 + 756 x73 + 360 x74 + 727 x75 + 544 x76 + 610 x77 + 499 x78
   + 538 x79 + 94 x80 + 967 x81 + 255 x82 + 288 x83 + 170 x84 + 289 x85
   + 285 x86 + 597 x87 + 828 x88 + 24 x89 + 49 x90 + 129 x91 + 742 x92
   + 774 x93 + 532 x94 + 396 x95 + 875 x96 + 958 x97 + 834 x98 + 120 x99
   + 313 x100 + 57 x101 + 511 x102 + 581 x103 + 223 x104 + 215 x105
   + 821 x106 + 850 x107 + 280 x108 + 421 x109 + 728 x110 + 40 x111
   + 690 x112 + 443 x113 + 777 x114 + 94 x115 + 963 x116 + 579 x117
   + 14 x118 + 868 x119 + 600 x120
Subject To
 Contrainte0: x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 <= 4.25
 Contrainte1: x9 + x10 + x11 + x12 + x13 + x14 + x15 + x16 <= 4.25
 Contrainte2: x17 + x18 + x19 + x20 + x21 + x22 + x23 + x24 <= 4.25
 Contrainte3: x25 + x26 + x27 + x28 + x29 + x30 + x31 + x32 <= 4.25
 Contrainte4: x33 + x34 + x35 + x36 + x37 + x38 + x39 + x40 <= 4.25
 Contrainte5: x41 + x42 + x43 + x44 + x45 + x46 + x47 + x48 <= 4.25
 Contrainte6: x49 + x50 + x51 + x52 + x53 + x54 + x55 + x56 <= 4.25
 Contrainte7: x57 + x58 + x59 + x60 + x61 + x62 + x63 + x64 <= 4.25
 Contrainte8: x65 + x66 + x67 + x68 + x69 + x70 + x71 + x72 <= 4.25
 Contrainte9: x73 + x74 + x75 + x76 + x77 + x78 + x79 + x80 <= 4.25
 Contrainte10: x81 + x82 + x83 + x84 + x85 + x86 + x87 + x88 <= 4.25
 Contrainte11: x89 + x90 + x91 + x92 + x93 + x94 + x95 + x96 <= 4.25
 Contrainte12: x97 + x98 + x99 + x100 + x101 + x102 + x103 + x104 <= 4.25
 Contrainte13: x105 + x106 + x107 + x108 + x109 + x110 + x111 + x112
   <= 4.25
 Contrainte14: x113 + x114 + x115 + x116 + x117 + x118 + x119 + x120
   <= 4.25
 Contrainte15: x1 + x9 + x17 + x25 + x33 + x41 + x49 + x57 + x65 + x73
   + x81 + x89 + x97 + x105 + x113 <= 2.266666666666667
 Contrainte16: x2 + x10 + x18 + x26 + x34 + x42 + x50 + x58 + x66 + x74
   + x82 + x90 + x98 + x106 + x114 <= 2.266666666666667
 Contrainte17: x3 + x11 + x19 + x27 + x35 + x43 + x51 + x59 + x67 + x75
   + x83 + x91 + x99 + x107 + x115 <= 2.266666666666667
 Contrainte18: x4 + x12 + x20 + x28 + x36 + x44 + x52 + x60 + x68 + x76
   + x84 + x92 + x100 + x108 + x116 <= 2.266666666666667
 Contrainte19: x5 + x13 + x21 + x29 + x37 + x45 + x53 + x61 + x69 + x77
   + x85 + x93 + x101 + x109 + x117 <= 2.266666666666667
 Contrainte20: x6 + x14 + x22 + x30 + x38 + x46 + x54 + x62 + x70 + x78
   + x86 + x94 + x102 + x110 + x118 <= 2.266666666666667
 Contrainte21: x7 + x15 + x23 + x31 + x39 + x47 + x55 + x63 + x71 + x79
   + x87 + x95 + x103 + x111 + x119 <= 2.266666666666667
 Contrainte22: x8 + x16 + x24 + x32 + x40 + x48 + x56 + x64 + x72 + x80
   + x88 + x96 + x104 + x112 + x120 <= 2.266666666666667
 Contrainte23: x1 + x3 <= 1
 Contrainte24: x2 + x4 <= 1
 Contrainte25: x3 + x5 <= 1
 Contrainte26: x4 + x6 <= 1
 Contrainte27: x5 + x7 <= 1
 Contrainte28: x6 + x8 <= 1
 Contrainte29: x9 + x11 <= 1
 Contrainte30: x10 + x12 <= 1
 Contrainte31: x11 + x13 <= 1
 Contrainte32: x12 + x14 <= 1
 Contrainte33: x13 + x15 <= 1
 Contrainte34: x14 + x16 <= 1
 Contrainte35: x17 + x19 <= 1
 Contrainte36: x18 + x20 <= 1
 Contrainte37: x19 + x21 <= 1
 Contrainte38: x20 + x22 <= 1
 Contrainte39: x21 + x23 <= 1
 Contrainte40: x22 + x24 <= 1
 Contrainte41: x25 + x27 <= 1
 Contrainte42: x26 + x28 <= 1
 Contrainte43: x27 + x29 <= 1
 Contrainte44: x28 + x30 <= 1
 Contrainte45: x29 + x31 <= 1
 Contrainte46: x30 + x32 <= 1
 Contrainte47: x33 + x35 <= 1
 Contrainte48: x34 + x36 <= 1
 Contrainte49: x35 + x37 <= 1
 Contrainte50: x36 + x38 <= 1
 Contrainte51: x37 + x39 <= 1
 Contrainte52: x38 + x40 <= 1
 Contrainte53: x41 + x43 <= 1
 Contrainte54: x42 + x44 <= 1
 Contrainte55: x43 + x45 <= 1
 Contrainte56: x44 + x46 <= 1
 Contrainte57: x45 + x47 <= 1
 Contrainte58: x46 + x48 <= 1
 Contrainte59: x49 + x51 <= 1
 Contrainte60: x50 + x52 <= 1
 Contrainte61: x51 + x53 <= 1
 Contrainte62: x52 + x54 <= 1
 Contrainte63: x53 + x55 <= 1
 Contrainte64: x54 + x56 <= 1
 Contrainte65: x57 + x59 <= 1
 Contrainte66: x58 + x60 <= 1
 Contrainte67: x59 + x61 <= 1
 Contrainte68: x60 + x62 <= 1
 Contrainte69: x61 + x63 <= 1
 Contrainte70: x62 + x64 <= 1
 Contrainte71: x65 + x67 <= 1
 Contrainte72: x66 + x68 <= 1
 Contrainte73: x67 + x69 <= 1
 Contrainte74: x68 + x70 <= 1
 Contrainte75: x69 + x71 <= 1
 Contrainte76: x70 + x72 <= 1
 Contrainte77: x73 + x75 <= 1
 Contrainte78: x74 + x76 <= 1
 Contrainte79: x75 + x77 <= 1
 Contrainte80: x76 + x78 <= 1
 Contrainte81: x77 + x79 <= 1
 Contrainte82: x78 + x80 <= 1
 Contrainte83: x81 + x83 <= 1
 Contrainte84: x82 + x84 <= 1
 Contrainte85: x83 + x85 <= 1
 Contrainte86: x84 + x86 <= 1
 Contrainte87: x85 + x87 <= 1
 Contrainte88: x86 + x88 <= 1
 Contrainte89: x89 + x91 <= 1
 Contrainte90: x90 + x92 <= 1
 Contrainte91: x91 + x93 <= 1
 Contrainte92: x92 + x94 <= 1
 Contrainte93: x93 + x95 <= 1
 Contrainte94: x94 + x96 <= 1
 Contrainte95: x97 + x99 <= 1
 Contrainte96: x98 + x100 <= 1
 Contrainte97: x99 + x101 <= 1
 Contrainte98: x100 + x102 <= 1
 Contrainte99: x101 + x103 <= 1
 Contrainte100: x102 + x104 <= 1
 Contrainte101: x105 + x107 <= 1
 Contrainte102: x106 + x108 <= 1
 Contrainte103: x107 + x109 <= 1
 Contrainte104: x108 + x110 <= 1
 Contrainte105: x109 + x111 <= 1
 Contrainte106: x110 + x112 <= 1
 Contrainte107: x113 + x115 <= 1
 Contrainte108: x114 + x116 <= 1
 Contrainte109: x115 + x117 <= 1
 Contrainte110: x116 + x118 <= 1
 Contrainte111: x117 + x119 <= 1
 Contrainte112: x118 + x120 <= 1
 Contrainte113: x1 + x17 <= 1
 Contrainte114: x2 + x18 <= 1
 Contrainte115: x3 + x19 <= 1
 Contrainte116: x4 + x20 <= 1
 Contrainte117: x5 + x21 <= 1
 Contrainte118: x6 + x22 <= 1
 Contrainte119: x7 + x23 <= 1
 Contrainte120: x8 + x24 <= 1
 Contrainte121: x9 + x25 <= 1
 Contrainte122: x10 + x26 <= 1
 Contrainte123: x11 + x27 <= 1
 Contrainte124: x12 + x28 <= 1
 Contrainte125: x13 + x29 <= 1
 Contrainte126: x14 + x30 <= 1
 Contrainte127: x15 + x31 <= 1
 Contrainte128: x16 + x32 <= 1
 Contrainte129: x17 + x33 <= 1
 Contrainte130: x18 + x34 <= 1
 Contrainte131: x19 + x35 <= 1
 Contrainte132: x20 + x36 <= 1
 Contrainte133: x21 + x37 <= 1
 Contrainte134: x22 + x38 <= 1
 Contrainte135: x23 + x39 <= 1
 Contrainte136: x24 + x40 <= 1
 Contrainte137: x25 + x41 <= 1
 Contrainte138: x26 + x42 <= 1
 Contrainte139: x27 + x43 <= 1
 Contrainte140: x28 + x44 <= 1
 Contrainte141: x29 + x45 <= 1
 Contrainte142: x30 + x46 <= 1
 Contrainte143: x31 + x47 <= 1
 Contrainte144: x32 + x48 <= 1
 Contrainte145: x33 + x49 <= 1
 Contrainte146: x34 + x50 <= 1
 Contrainte147: x35 + x51 <= 1
 Contrainte148: x36 + x52 <= 1
 Contrainte149: x37 + x53 <= 1
 Contrainte150: x38 + x54 <= 1
 Contrainte151: x39 + x55 <= 1
 Contrainte152: x40 + x56 <= 1
 Contrainte153: x41 + x57 <= 1
 Contrainte154: x42 + x58 <= 1
 Contrainte155: x43 + x59 <= 1
 Contrainte156: x44 + x60 <= 1
 Contrainte157: x45 + x61 <= 1
 Contrainte158: x46 + x62 <= 1
 Contrainte159: x47 + x63 <= 1
 Contrainte160: x48 + x64 <= 1
 Contrainte161: x49 + x65 <= 1
 Contrainte162: x50 + x66 <= 1
 Contrainte163: x51 + x67 <= 1
 Contrainte164: x52 + x68 <= 1
 Contrainte165: x53 + x69 <= 1
 Contrainte166: x54 + x70 <= 1
 Contrainte167: x55 + x71 <= 1
 Contrainte168: x56 + x72 <= 1
 Contrainte169: x57 + x73 <= 1
 Contrainte170: x58 + x74 <= 1
 Contrainte171: x59 + x75 <= 1
 Contrainte172: x60 + x76 <= 1
 Contrainte173: x61 + x77 <= 1
 Contrainte174: x62 + x78 <= 1
 Contrainte175: x63 + x79 <= 1
 Contrainte176: x64 + x80 <= 1
 Contrainte177: x65 + x81 <= 1
 Contrainte178: x66 + x82 <= 1
 Contrainte179: x67 + x83 <= 1
 Contrainte180: x68 + x84 <= 1
 Contrainte181: x69 + x85 <= 1
 Contrainte182: x70 + x86 <= 1
 Contrainte183: x71 + x87 <= 1
 Contrainte184: x72 + x88 <= 1
 Contrainte185: x73 + x89 <= 1
 Contrainte186: x74 + x90 <= 1
 Contrainte187: x75 + x91 <= 1
 Contrainte188: x76 + x92 <= 1
 Contrainte189: x77 + x93 <= 1
 Contrainte190: x78 + x94 <= 1
 Contrainte191: x79 + x95 <= 1
 Contrainte192: x80 + x96 <= 1
 Contrainte193: x81 + x97 <= 1
 Contrainte194: x82 + x98 <= 1
 Contrainte195: x83 + x99 <= 1
 Contrainte196: x84 + x100 <= 1
 Contrainte197: x85 + x101 <= 1
 Contrainte198: x86 + x102 <= 1
 Contrainte199: x87 + x103 <= 1
 Contrainte200: x88 + x104 <= 1
 Contrainte201: x89 + x105 <= 1
 Contrainte202: x90 + x106 <= 1
 Contrainte203: x91 + x107 <= 1
 Contrainte204: x92 + x108 <= 1
 Contrainte205: x93 + x109 <= 1
 Contrainte206: x94 + x110 <= 1
 Contrainte207: x95 + x111 <= 1
 Contrainte208: x96 + x112 <= 1
 Contrainte209: x97 + x113 <= 1
 Contrainte210: x98 + x114 <= 1
 Contrainte211: x99 + x115 <= 1
 Contrainte212: x100 + x116 <= 1
 Contrainte213: x101 + x117 <= 1
 Contrainte214: x102 + x118 <= 1
 Contrainte215: x103 + x119 <= 1
 Contrainte216: x104 + x120 <= 1
 Contrainte217: - x1 - x2 - x3 - x4 - x5 - x6 - x7 - x8 - x9 - x10 - x11
   - x12 - x13 - x14 - x15 - x16 - x17 - x18 - x19 - x20 - x21 - x22 - x23
   - x24 - x25 - x26 - x27 - x28 - x29 - x30 - x31 - x32 - x33 - x34 - x35
   - x36 - x37 - x38 - x39 - x40 - x41 - x42 - x43 - x44 - x45 - x46 - x47
   - x48 - x49 - x50 - x51 - x52 - x53 - x54 - x55 - x56 - x57 - x58 - x59
   - x60 - x61 - x62 - x63 - x64 - x65 - x66 - x67 - x68 - x69 - x70 - x71
   - x72 - x73 - x74 - x75 - x76 - x77 - x78 - x79 - x80 - x81 - x82 - x83
   - x84 - x85 - x86 - x87 - x88 - x89 - x90 - x91 - x92 - x93 - x94 - x95
   - x96 - x97 - x98 - x99 - x100 - x101 - x102 - x103 - x104 - x105 - x106
   - x107 - x108 - x109 - x110 - x111 - x112 - x113 - x114 - x115 - x116
   - x117 - x118 - x119 - x120 <= -17
Bounds
Binaries
 x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15 x16 x17 x18 x19 x20 x21
 x22 x23 x24 x25 x26 x27 x28 x29 x30 x31 x32 x33 x34 x35 x36 x37 x38 x39
 x40 x41 x42 x43 x44 x45 x46 x47 x48 x49 x50 x51 x52 x53 x54 x55 x56 x57
 x58 x59 x60 x61 x62 x63 x64 x65 x66 x67 x68 x69 x70 x71 x72 x73 x74 x75
 x76 x77 x78 x79 x80 x81 x82 x83 x84 x85 x86 x87 x88 x89 x90 x91 x92 x93
 x94 x95 x96 x97 x98 x99 x100 x101 x102 x103 x104 x105 x106 x107 x108 x109
 x110 x111 x112 x113 x114 x115 x116 x117 x118 x119 x120
End
