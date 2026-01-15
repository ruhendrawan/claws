import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt
from traitlets import Long

data = """batch_id,gold_view,threshold,precision_macro,recall_macro,f1_macro,jaccard_macro,exact_accuracy_macro,precision_micro,recall_micro,f1_micro,jaccard_micro
"""

# data += """
# splits_window_5_code_with_problems/chars_bin=0,parser,5,0.9121,0.9014,0.9032,0.8320,0.1894,0.9010,0.9043,0.9027,0.8226
# splits_window_5_code_with_problems/chars_bin=1,parser,5,0.8819,0.8838,0.8803,0.8126,0.0458,0.8837,0.9071,0.8952,0.8103
# splits_window_5_code_with_problems/comments_bin=0,parser,5,0.9135,0.9001,0.9033,0.8320,0.1739,0.9011,0.9023,0.9017,0.8210
# splits_window_5_code_with_problems/comments_bin=1,parser,5,0.8790,0.8844,0.8791,0.8118,0.0560,0.8815,0.9092,0.8951,0.8102
# splits_window_5_code_with_problems/length_lines_bin=0,parser,5,0.9137,0.8958,0.9008,0.8278,0.1748,0.9032,0.8972,0.9002,0.8185
# splits_window_5_code_with_problems/length_lines_bin=1,parser,5,0.8773,0.8888,0.8811,0.8158,0.0500,0.8810,0.9127,0.8966,0.8126
# splits_window_5_code_with_problems/chars_bin=0,parser,4,0.8803,0.9741,0.9210,0.8602,0.2197,0.8620,0.9742,0.9147,0.8428
# splits_window_5_code_with_problems/chars_bin=1,parser,4,0.8518,0.9335,0.8893,0.8267,0.0840,0.8506,0.9555,0.9000,0.8182
# splits_window_5_code_with_problems/comments_bin=0,parser,4,0.8771,0.9656,0.9157,0.8511,0.1884,0.8589,0.9649,0.9088,0.8329
# splits_window_5_code_with_problems/comments_bin=1,parser,4,0.8540,0.9409,0.8936,0.8352,0.1120,0.8519,0.9610,0.9032,0.8234
# splits_window_5_code_with_problems/length_lines_bin=0,parser,4,0.8871,0.9698,0.9230,0.8631,0.2098,0.8721,0.9693,0.9181,0.8486
# splits_window_5_code_with_problems/length_lines_bin=1,parser,4,0.8411,0.9348,0.8840,0.8202,0.0833,0.8425,0.9579,0.8965,0.8124
# splits_window_5_code_with_problems/chars_bin=0,parser,3,0.8233,0.9768,0.8885,0.8077,0.1288,0.8044,0.9772,0.8824,0.7895
# splits_window_5_code_with_problems/chars_bin=1,parser,3,0.8272,0.9393,0.8780,0.8076,0.0534,0.8277,0.9607,0.8892,0.8006
# splits_window_5_code_with_problems/comments_bin=0,parser,3,0.8292,0.9693,0.8895,0.8085,0.1159,0.8128,0.9687,0.8839,0.7920
# splits_window_5_code_with_problems/comments_bin=1,parser,3,0.8208,0.9458,0.8764,0.8066,0.0640,0.8230,0.9658,0.8887,0.7997
# splits_window_5_code_with_problems/length_lines_bin=0,parser,3,0.8306,0.9740,0.8917,0.8122,0.1189,0.8146,0.9740,0.8872,0.7973
# splits_window_5_code_with_problems/length_lines_bin=1,parser,3,0.8188,0.9392,0.8732,0.8022,0.0583,0.8211,0.9619,0.8860,0.7953
# """

data += """
splits_window_5_code_with_problems/chars_bin=0,parser,3,0.8233,0.9768,0.8885,0.8077,0.1288,0.8044,0.9772,0.8824,0.7895
splits_window_5_code_with_problems/chars_bin=1,parser,3,0.8272,0.9393,0.8780,0.8076,0.0534,0.8277,0.9607,0.8892,0.8006
splits_window_5_code_with_problems/comments_bin=0,parser,3,0.8292,0.9693,0.8895,0.8085,0.1159,0.8128,0.9687,0.8839,0.7920
splits_window_5_code_with_problems/comments_bin=1,parser,3,0.8208,0.9458,0.8764,0.8066,0.0640,0.8230,0.9658,0.8887,0.7997
splits_window_5_code_with_problems/length_lines_bin=0,parser,3,0.8306,0.9740,0.8917,0.8122,0.1189,0.8146,0.9740,0.8872,0.7973
splits_window_5_code_with_problems/length_lines_bin=1,parser,3,0.8188,0.9392,0.8732,0.8022,0.0583,0.8211,0.9619,0.8860,0.7953
splits_window_5_code_with_problems/chars_bin=0,parser,4,0.8803,0.9741,0.9210,0.8602,0.2197,0.8620,0.9742,0.9147,0.8428
splits_window_5_code_with_problems/chars_bin=1,parser,4,0.8518,0.9335,0.8893,0.8267,0.0840,0.8506,0.9555,0.9000,0.8182
splits_window_5_code_with_problems/comments_bin=0,parser,4,0.8771,0.9656,0.9157,0.8511,0.1884,0.8589,0.9649,0.9088,0.8329
splits_window_5_code_with_problems/comments_bin=1,parser,4,0.8540,0.9409,0.8936,0.8352,0.1120,0.8519,0.9610,0.9032,0.8234
splits_window_5_code_with_problems/length_lines_bin=0,parser,4,0.8871,0.9698,0.9230,0.8631,0.2098,0.8721,0.9693,0.9181,0.8486
splits_window_5_code_with_problems/length_lines_bin=1,parser,4,0.8411,0.9348,0.8840,0.8202,0.0833,0.8425,0.9579,0.8965,0.8124
splits_window_5_code_with_problems/chars_bin=0,parser,5,0.9121,0.9014,0.9032,0.8320,0.1894,0.9010,0.9043,0.9027,0.8226
splits_window_5_code_with_problems/chars_bin=1,parser,5,0.8819,0.8838,0.8803,0.8126,0.0458,0.8837,0.9071,0.8952,0.8103
splits_window_5_code_with_problems/comments_bin=0,parser,5,0.9135,0.9001,0.9033,0.8320,0.1739,0.9011,0.9023,0.9017,0.8210
splits_window_5_code_with_problems/comments_bin=1,parser,5,0.8790,0.8844,0.8791,0.8118,0.0560,0.8815,0.9092,0.8951,0.8102
splits_window_5_code_with_problems/length_lines_bin=0,parser,5,0.9137,0.8958,0.9008,0.8278,0.1748,0.9032,0.8972,0.9002,0.8185
splits_window_5_code_with_problems/length_lines_bin=1,parser,5,0.8773,0.8888,0.8811,0.8158,0.0500,0.8810,0.9127,0.8966,0.8126
"""

data += """
splits_window_10_code_with_problems/chars_bin=0,parser,5,0.8974,0.8566,0.8707,0.7798,0.0758,0.8832,0.8624,0.8727,0.7741
splits_window_10_code_with_problems/chars_bin=1,parser,5,0.8543,0.8670,0.8583,0.7778,0.0229,0.8568,0.8934,0.8747,0.7773
splits_window_10_code_with_problems/comments_bin=0,parser,5,0.8864,0.8610,0.8680,0.7753,0.0580,0.8723,0.8690,0.8707,0.7710
splits_window_10_code_with_problems/comments_bin=1,parser,5,0.8644,0.8626,0.8608,0.7827,0.0400,0.8622,0.8916,0.8766,0.7804
splits_window_10_code_with_problems/length_lines_bin=0,parser,5,0.8982,0.8515,0.8687,0.7762,0.0629,0.8860,0.8558,0.8706,0.7709
splits_window_10_code_with_problems/length_lines_bin=1,parser,5,0.8494,0.8740,0.8595,0.7819,0.0333,0.8534,0.9006,0.8763,0.7799
splits_window_10_code_with_problems/chars_bin=0,parser,4,0.8437,0.9763,0.9018,0.8285,0.1288,0.8298,0.9757,0.8969,0.8130
splits_window_10_code_with_problems/chars_bin=1,parser,4,0.8041,0.9290,0.8601,0.7802,0.0458,0.8058,0.9498,0.8719,0.7728
splits_window_10_code_with_problems/comments_bin=0,parser,4,0.8374,0.9703,0.8956,0.8185,0.1159,0.8237,0.9687,0.8903,0.8023
splits_window_10_code_with_problems/comments_bin=1,parser,4,0.8092,0.9333,0.8649,0.7890,0.0560,0.8080,0.9525,0.8743,0.7767
splits_window_10_code_with_problems/length_lines_bin=0,parser,4,0.8455,0.9720,0.9009,0.8269,0.1399,0.8341,0.9700,0.8969,0.8131
splits_window_10_code_with_problems/length_lines_bin=1,parser,4,0.7984,0.9297,0.8574,0.7778,0.0250,0.8011,0.9523,0.8702,0.7702
splits_window_10_code_with_problems/chars_bin=0,parser,3,0.8153,0.9810,0.8865,0.8037,0.0985,0.7987,0.9809,0.8804,0.7864
splits_window_10_code_with_problems/chars_bin=1,parser,3,0.7799,0.9316,0.8469,0.7594,0.0305,0.7823,0.9521,0.8589,0.7527
splits_window_10_code_with_problems/comments_bin=0,parser,3,0.8113,0.9750,0.8818,0.7961,0.0797,0.7961,0.9737,0.8760,0.7793
splits_window_10_code_with_problems/comments_bin=1,parser,3,0.7826,0.9359,0.8501,0.7656,0.0480,0.7825,0.9546,0.8600,0.7544
splits_window_10_code_with_problems/length_lines_bin=0,parser,3,0.8145,0.9774,0.8847,0.8008,0.0979,0.8002,0.9760,0.8794,0.7848
splits_window_10_code_with_problems/length_lines_bin=1,parser,3,0.7775,0.9313,0.8454,0.7587,0.0250,0.7801,0.9538,0.8583,0.7517
"""

data += """
splits_no_window_code_with_problems/chars_bin=0,parser,3,0.9047,0.9151,0.9052,0.8520,0.3030,0.9158,0.9124,0.9141,0.8418
splits_no_window_code_with_problems/chars_bin=1,parser,3,0.8833,0.9089,0.8936,0.8403,0.1145,0.8921,0.9284,0.9099,0.8347
splits_no_window_code_with_problems/comments_bin=0,parser,3,0.8954,0.9030,0.8945,0.8378,0.2609,0.9089,0.8997,0.9043,0.8253
splits_no_window_code_with_problems/comments_bin=1,parser,3,0.8926,0.9219,0.9050,0.8555,0.1520,0.8949,0.9413,0.9175,0.8476
splits_no_window_code_with_problems/length_lines_bin=0,parser,3,0.9086,0.9185,0.9090,0.8571,0.3217,0.9183,0.9159,0.9171,0.8469
splits_no_window_code_with_problems/length_lines_bin=1,parser,3,0.8767,0.9043,0.8881,0.8332,0.0750,0.8886,0.9269,0.9074,0.8305
splits_no_window_code_with_problems/chars_bin=0,parser,4,0.9109,0.9143,0.9083,0.8568,0.3030,0.9246,0.9117,0.9181,0.8486
splits_no_window_code_with_problems/chars_bin=1,parser,4,0.8915,0.9079,0.8974,0.8464,0.1145,0.9002,0.9275,0.9136,0.8410
splits_no_window_code_with_problems/comments_bin=0,parser,4,0.9027,0.9022,0.8981,0.8435,0.2609,0.9181,0.8991,0.9085,0.8324
splits_no_window_code_with_problems/comments_bin=1,parser,4,0.8996,0.9209,0.9081,0.8606,0.1520,0.9026,0.9402,0.9210,0.8536
splits_no_window_code_with_problems/length_lines_bin=0,parser,4,0.9148,0.9177,0.9121,0.8619,0.3217,0.9270,0.9152,0.9211,0.8537
splits_no_window_code_with_problems/length_lines_bin=1,parser,4,0.8851,0.9032,0.8919,0.8395,0.0750,0.8968,0.9259,0.9111,0.8368
splits_no_window_code_with_problems/chars_bin=0,parser,5,0.9335,0.8684,0.8935,0.8330,0.2652,0.9472,0.8705,0.9072,0.8302
splits_no_window_code_with_problems/chars_bin=1,parser,5,0.9045,0.8943,0.8969,0.8465,0.1298,0.9139,0.9152,0.9145,0.8425
splits_no_window_code_with_problems/comments_bin=0,parser,5,0.9217,0.8666,0.8874,0.8262,0.2246,0.9383,0.8678,0.9017,0.8210
splits_no_window_code_with_problems/comments_bin=1,parser,5,0.9162,0.8975,0.9038,0.8547,0.1680,0.9168,0.9231,0.9199,0.8517
splits_no_window_code_with_problems/length_lines_bin=0,parser,5,0.9354,0.8761,0.8986,0.8404,0.2937,0.9474,0.8778,0.9113,0.8370
splits_no_window_code_with_problems/length_lines_bin=1,parser,5,0.8996,0.8875,0.8912,0.8389,0.0833,0.9113,0.9127,0.9120,0.8383
"""

data += """
splits_window_50_code_with_problems/chars_bin=0,parser,5,0.9386,0.8805,0.9036,0.8318,0.0985,0.9313,0.8874,0.9088,0.8329
splits_window_50_code_with_problems/chars_bin=1,parser,5,0.9066,0.8898,0.8964,0.8391,0.0458,0.9081,0.9137,0.9109,0.8364
splits_window_50_code_with_problems/comments_bin=0,parser,5,0.9335,0.8877,0.9049,0.8336,0.0942,0.9219,0.8947,0.9081,0.8317
splits_window_50_code_with_problems/comments_bin=1,parser,5,0.9107,0.8822,0.8947,0.8374,0.0480,0.9128,0.9108,0.9118,0.8379
splits_window_50_code_with_problems/length_lines_bin=0,parser,5,0.9387,0.8807,0.9040,0.8322,0.0769,0.9319,0.8865,0.9087,0.8326
splits_window_50_code_with_problems/length_lines_bin=1,parser,5,0.9034,0.8903,0.8953,0.8393,0.0667,0.9062,0.9163,0.9112,0.8369
splits_window_50_code_with_problems/chars_bin=0,parser,4,0.9156,0.9574,0.9311,0.8779,0.2652,0.9049,0.9588,0.9310,0.8710
splits_window_50_code_with_problems/chars_bin=1,parser,4,0.8881,0.9297,0.9073,0.8574,0.0992,0.8895,0.9502,0.9189,0.8499
splits_window_50_code_with_problems/comments_bin=0,parser,4,0.9080,0.9510,0.9242,0.8662,0.2319,0.8946,0.9524,0.9226,0.8563
splits_window_50_code_with_problems/comments_bin=1,parser,4,0.8952,0.9355,0.9137,0.8694,0.1280,0.8962,0.9546,0.9245,0.8596
splits_window_50_code_with_problems/length_lines_bin=0,parser,4,0.9194,0.9566,0.9330,0.8814,0.2727,0.9105,0.9579,0.9336,0.8755
splits_window_50_code_with_problems/length_lines_bin=1,parser,4,0.8810,0.9283,0.9028,0.8514,0.0750,0.8843,0.9503,0.9161,0.8452
splits_window_50_code_with_problems/chars_bin=0,parser,3,0.9039,0.9594,0.9256,0.8684,0.2273,0.8933,0.9610,0.9259,0.8620
splits_window_50_code_with_problems/chars_bin=1,parser,3,0.8830,0.9318,0.9055,0.8542,0.0916,0.8846,0.9521,0.9171,0.8470
splits_window_50_code_with_problems/comments_bin=0,parser,3,0.8962,0.9529,0.9186,0.8565,0.2029,0.8834,0.9543,0.9175,0.8475
splits_window_50_code_with_problems/comments_bin=1,parser,3,0.8905,0.9378,0.9122,0.8666,0.1120,0.8920,0.9568,0.9232,0.8574
splits_window_50_code_with_problems/length_lines_bin=0,parser,3,0.9074,0.9584,0.9273,0.8714,0.2308,0.8982,0.9599,0.9280,0.8657
splits_window_50_code_with_problems/length_lines_bin=1,parser,3,0.8768,0.9306,0.9016,0.8493,0.0750,0.8804,0.9523,0.9149,0.8432
"""




data += """
splits_window_25_code_with_problems/chars_bin=0,parser,3,0.9084,0.9752,0.9367,0.8896,0.3561,0.9005,0.9728,0.9353,0.8784
splits_window_25_code_with_problems/chars_bin=1,parser,3,0.8847,0.9282,0.9042,0.8531,0.0992,0.8880,0.9474,0.9168,0.8463
splits_window_25_code_with_problems/comments_bin=0,parser,3,0.9065,0.9624,0.9299,0.8785,0.3188,0.8961,0.9568,0.9255,0.8613
splits_window_25_code_with_problems/comments_bin=1,parser,3,0.8857,0.9400,0.9101,0.8636,0.1280,0.8903,0.9578,0.9228,0.8567
splits_window_25_code_with_problems/length_lines_bin=0,parser,3,0.9092,0.9725,0.9360,0.8881,0.3427,0.9024,0.9693,0.9347,0.8773
splits_window_25_code_with_problems/length_lines_bin=1,parser,3,0.8816,0.9270,0.9020,0.8516,0.0917,0.8858,0.9482,0.9160,0.8449
splits_window_25_code_with_problems/chars_bin=0,parser,4,0.9267,0.9727,0.9455,0.9042,0.3939,0.9204,0.9698,0.9445,0.8948
splits_window_25_code_with_problems/chars_bin=1,parser,4,0.8927,0.9215,0.9054,0.8553,0.1145,0.8970,0.9412,0.9186,0.8494
splits_window_25_code_with_problems/comments_bin=0,parser,4,0.9224,0.9591,0.9368,0.8902,0.3696,0.9135,0.9530,0.9328,0.8741
splits_window_25_code_with_problems/comments_bin=1,parser,4,0.8959,0.9340,0.9131,0.8685,0.1280,0.9001,0.9519,0.9253,0.8609
splits_window_25_code_with_problems/length_lines_bin=0,parser,4,0.9269,0.9684,0.9436,0.9007,0.3846,0.9216,0.9646,0.9426,0.8914
splits_window_25_code_with_problems/length_lines_bin=1,parser,4,0.8894,0.9219,0.9039,0.8550,0.1000,0.8946,0.9432,0.9183,0.8489
splits_window_25_code_with_problems/chars_bin=0,parser,5,0.9481,0.9294,0.9341,0.8840,0.3258,0.9444,0.9257,0.9350,0.8779
splits_window_25_code_with_problems/chars_bin=1,parser,5,0.9080,0.8925,0.8983,0.8435,0.1069,0.9123,0.9123,0.9123,0.8388
splits_window_25_code_with_problems/comments_bin=0,parser,5,0.9437,0.9132,0.9239,0.8675,0.2754,0.9367,0.9091,0.9227,0.8566
splits_window_25_code_with_problems/comments_bin=1,parser,5,0.9110,0.9086,0.9077,0.8598,0.1520,0.9149,0.9247,0.9198,0.8515
splits_window_25_code_with_problems/length_lines_bin=0,parser,5,0.9462,0.9273,0.9320,0.8804,0.3077,0.9427,0.9226,0.9325,0.8736
splits_window_25_code_with_problems/length_lines_bin=1,parser,5,0.9066,0.8915,0.8974,0.8441,0.1083,0.9114,0.9137,0.9126,0.8392
"""

df = pd.read_csv(StringIO(data))


# SUMMARY_CSV_FILE = "output/accuracy_summary.csv"

# df = pd.read_csv(SUMMARY_CSV_FILE)
print(df.head())


def parse_batch_id(s: str):
    window = "window_5" if "window_5_" in s else "window_10" if "window_10_" in s else "window_25" if "window_25_" in s else "window_50" if "window_50_" in s else "no_window" if "no_window_" in s else "window_unknown"
    bin_info = s.split("/")[-1]
    bin_type, bin_val = bin_info.split("=")
    pretty_bin = {"chars_bin":"Chars", "comments_bin":"Comments", "length_lines_bin":"Length Lines"}
    pretty_val = {
        "chars_bin": {"0":"Short", "1":"Long"},
        "comments_bin": {"0":"Few", "1":"Many"},
        "length_lines_bin": {"0":"Short", "1":"Long"}
    }
    label = f"{pretty_bin.get(bin_type, bin_type)}={pretty_val[bin_type].get(bin_val, bin_val)}"
    return window, bin_type, bin_val, label

df[["window","bin_type","bin_val","label"]] = df["batch_id"].apply(lambda x: pd.Series(parse_batch_id(x)))

df = df[df["bin_type"] != "length_lines_bin"]
df = df[df["threshold"].isin([4])]
df = df[df["window"].isin(["window_5","window_10","no_window"])]

colors_bin = {"chars_bin":"tab:blue", "comments_bin":"tab:red", "length_lines_bin":"tab:green"}
shapes_window = {"window_5":"o", "window_10":"^", "window_25": "D", "window_50":"P", "no_window":"s", "window_unknown":"D"}



def scatter_with_cross_contrast(x_col, y_col, title, xlim, ylim, xlabel, ylabel):
    plt.figure(figsize=(10,7))
    for _, row in df.iterrows():
        marker = shapes_window[row["window"]]
        color = colors_bin[row["bin_type"]]
        is_low = str(row["bin_val"]) == "0"
        if row["threshold"] == 4:
            plt.scatter(row[x_col], row[y_col], marker=marker, s=140,
                        color=color, edgecolors='black', linewidths=0.8, alpha=0.9, zorder=2)
        elif row["threshold"] == 5:
            plt.scatter(row[x_col], row[y_col], marker=marker, s=140,
                        facecolors='none', edgecolors=color, linewidths=1.6, alpha=0.9, zorder=2)
        elif row["threshold"] == 3:
            plt.scatter(row[x_col], row[y_col], marker=marker, s=140,
                        facecolors='gray', edgecolors='black', linewidths=0.8, alpha=0.5, zorder=1)
        if is_low:
            plt.scatter(row[x_col], row[y_col], marker="x", s=60,
                        color="black", linewidths=1.2, zorder=3)
        # plt.text(row[x_col]+0.001, row[y_col], row["label"], fontsize=8)
        plt.text(row[x_col]+0.001, row[y_col]-0.001, f"{row['window'].replace('window_','w')},t{row['threshold']}", fontsize=8)

    # Connect low↔high separately per bin type for each window size and threshold
    for (bin_type, bin_val, window, threshold), group in df.groupby(["bin_type","bin_val","window","threshold"]):
        if bin_val == "0":
            high_row = df[(df["bin_type"]==bin_type) & (df["bin_val"]=="1") & (df["window"]==window) & (df["threshold"]==threshold)]
            if not high_row.empty:
                plt.plot([group.iloc[0][x_col], high_row.iloc[0][x_col]],
                         [group.iloc[0][y_col], high_row.iloc[0][y_col]],
                         color='gray', linestyle='--', linewidth=1, alpha=0.5, zorder=0)
        elif bin_val == "1":
            low_row = df[(df["bin_type"]==bin_type) & (df["bin_val"]=="0") & (df["window"]==window) & (df["threshold"]==threshold)]
            if not low_row.empty:
                plt.plot([low_row.iloc[0][x_col], group.iloc[0][x_col]],
                         [low_row.iloc[0][y_col], group.iloc[0][y_col]],
                         color='gray', linestyle='--', linewidth=1, alpha=0.5, zorder=0)


    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xlim(*xlim)
    plt.ylim(*ylim)
    plt.grid(True, linestyle="--", alpha=0.5)
    # Legend
    handles = []
    labels = []
    handles.append(plt.Line2D([0],[0], marker='o', linestyle='', color='w',
        markerfacecolor=colors_bin["chars_bin"], markeredgecolor='black', markersize=10))
    labels.append("Chars (Blue)")
    handles.append(plt.Line2D([0],[0], marker='o', linestyle='', color='w',
        markerfacecolor=colors_bin["comments_bin"], markeredgecolor='black', markersize=10))
    labels.append("Comments (Red)")
    handles.append(plt.Line2D([0],[0], marker='o', linestyle='', color='w',
        markerfacecolor='gray', markeredgecolor='black', markersize=10))
    labels.append("Threshold=4 (filled)")
    handles.append(plt.Line2D([0],[0], marker='o', linestyle='', color='w',
        markerfacecolor='none', markeredgecolor='black', markersize=10))
    labels.append("Threshold=5 (outline)")
    handles.append(plt.Line2D([0],[0], marker=shapes_window["window_5"], linestyle='', color='w',
        markerfacecolor='gray', markeredgecolor='black', markersize=10))
    labels.append("Window=5")
    handles.append(plt.Line2D([0],[0], marker=shapes_window["window_10"], linestyle='', color='w',
        markerfacecolor='gray', markeredgecolor='black', markersize=10))
    labels.append("Window=10")
    # handles.append(plt.Line2D([0],[0], marker=shapes_window["window_50"], linestyle='', color='w',
    #     markerfacecolor='gray', markeredgecolor='black', markersize=10))
    # labels.append("Window=50 (pentagon)")
    handles.append(plt.Line2D([0],[0], marker=shapes_window["no_window"], linestyle='', color='w',
        markerfacecolor='gray', markeredgecolor='black', markersize=10))
    labels.append("No Window")
    handles.append(plt.Line2D([0],[0], marker='x', color='black', linestyle='', markersize=8))
    labels.append("Low/Small bin (cross overlay)")
    plt.legend(handles, labels, title="Legend", loc="lower left", bbox_to_anchor=(1.01,0))
    plt.tight_layout()
    plt.show()


min_max_precision = (df["precision_macro"].min()-0.01, df["precision_macro"].max()+0.01)
min_max_recall = (df["recall_macro"].min()-0.01, df["recall_macro"].max()+0.01)
min_max_f1 = (df["f1_macro"].min()-0.01, df["f1_macro"].max()+0.01)
min_max_exact = (df["exact_accuracy_macro"].min()-0.01, df["exact_accuracy_macro"].max()+0.01)

# Precision vs Recall
scatter_with_cross_contrast(
    x_col="precision_macro", y_col="recall_macro",
    title="Precision vs Recall",
    xlim=(min_max_precision), ylim=(min_max_recall),
    xlabel="Precision (macro)", ylabel="Recall (macro)"
)

# F1 vs Exact Accuracy
scatter_with_cross_contrast(
    x_col="f1_macro", y_col="exact_accuracy_macro",
    title="F1 vs Exact Accuracy",
    xlim=(min_max_f1), ylim=(min_max_exact),
    xlabel="F1 Macro", ylabel="Exact Accuracy Macro"
)
