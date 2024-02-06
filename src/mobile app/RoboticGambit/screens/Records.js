import * as React from "react";
import {
  ImageBackground,
  StyleSheet,
  Text,
  ScrollView,
  View,
} from "react-native";
import { Image } from "expo-image";
import { Button } from "react-native-paper";
import { useNavigation } from "@react-navigation/native";
import { Color, FontFamily, FontSize } from "../GlobalStyles";

const Records = () => {
  const navigation = useNavigation();

  return (
    <View style={styles.records}>
      <ImageBackground
        style={styles.dallE20231030213013IIcon}
        resizeMode="cover"
        source={require("../assets/dalle20231030213013illustrationofastreamlinedlogoforroboticgambit11.png")}
      />
      <Image
        style={styles.recordsChild}
        contentFit="cover"
        source={require("../assets/rectangle-1.png")}
      />
      <Text style={[styles.player, styles.pgnFlexBox]}>Player</Text>
      <Text style={[styles.date, styles.pgnFlexBox]}>Date</Text>
      <Text style={[styles.duration, styles.pgnFlexBox]}>Duration</Text>
      <Text style={[styles.result, styles.pgnFlexBox]}>Result</Text>
      <Text style={[styles.pgn, styles.pgnFlexBox]}>PGN</Text>
      <Text style={[styles.matchid, styles.pgnFlexBox]}>MatchID</Text>
      <ScrollView
        style={styles.recordData}
        showsVerticalScrollIndicator={true}
        showsHorizontalScrollIndicator={true}
      >
        <Text style={[styles.abdulqadir1124414, styles.abdulqadirTypo]}>
          Abdulqadir 11/24 4:14 Win 134321
        </Text>
        <ImageBackground
          style={[styles.image1Icon, styles.iconLayout]}
          resizeMode="cover"
          source={require("../assets/image1.png")}
        />
        <Text style={[styles.wadie1124614, styles.abdulqadirTypo]}>
          Wadie 11/24 6:14 Win 134320
        </Text>
        <ImageBackground
          style={[styles.image2Icon, styles.iconLayout]}
          resizeMode="cover"
          source={require("../assets/image1.png")}
        />
        <Text style={[styles.abdulaziz1123732, styles.abdulqadirTypo]}>
          Abdulaziz 11/23 7:32 Lose 134319
        </Text>
        <ImageBackground
          style={[styles.image3Icon, styles.iconLayout]}
          resizeMode="cover"
          source={require("../assets/image1.png")}
        />
        <Text style={[styles.ahmed1123444, styles.abdulqadirTypo]}>
          Ahmed 11/23 4:44 Win 134318
        </Text>
        <ImageBackground
          style={[styles.image4Icon, styles.iconLayout]}
          resizeMode="cover"
          source={require("../assets/image1.png")}
        />
        <Text style={[styles.rakan1122635, styles.abdulqadirTypo]}>
          Rakan 11/22 6:35 Win 134317
        </Text>
        <ImageBackground
          style={[styles.image5Icon, styles.iconLayout]}
          resizeMode="cover"
          source={require("../assets/image1.png")}
        />
        <Text style={[styles.waleed1122918, styles.abdulqadirTypo]}>
          Waleed 11/22 9:18 Lose 134316
        </Text>
        <ImageBackground
          style={[styles.image6Icon, styles.iconLayout]}
          resizeMode="cover"
          source={require("../assets/image1.png")}
        />
        <Text style={[styles.faisal1122817, styles.abdulqadirTypo]}>
          Faisal 11/22 8:17 Lose 134315
        </Text>
        <ImageBackground
          style={[styles.image7Icon, styles.iconLayout]}
          resizeMode="cover"
          source={require("../assets/image1.png")}
        />
        <Text style={[styles.ibrahim1121735, styles.abdulqadirTypo]}>
          Ibrahim 11/21 7:35 Lose 134314
        </Text>
        <ImageBackground
          style={[styles.image8Icon, styles.iconLayout]}
          resizeMode="cover"
          source={require("../assets/image1.png")}
        />
        <Text style={[styles.saad1121451, styles.abdulqadirTypo]}>
          Saad 11/21 4:51 Lose 134313
        </Text>
        <ImageBackground
          style={[styles.image9Icon, styles.iconLayout]}
          resizeMode="cover"
          source={require("../assets/image1.png")}
        />
        <Text style={[styles.shaker1121334, styles.abdulqadirTypo]}>
          Shaker 11/21 3:34 Lose 134312
        </Text>
        <ImageBackground
          style={[styles.image10Icon, styles.iconLayout]}
          resizeMode="cover"
          source={require("../assets/image1.png")}
        />
        <Text style={[styles.hussain1121912, styles.abdulqadirTypo]}>
          Hussain 11/21 9:12 Win 134311
        </Text>
        <ImageBackground
          style={[styles.image11Icon, styles.iconLayout]}
          resizeMode="cover"
          source={require("../assets/image1.png")}
        />
        <Text style={[styles.ali1121842, styles.abdulqadirTypo]}>
          Ali 11/21 8:42 Lose 134310
        </Text>
        <ImageBackground
          style={[styles.image12Icon, styles.iconLayout]}
          resizeMode="cover"
          source={require("../assets/image1.png")}
        />
        <Text style={[styles.nasser1120931, styles.abdulqadirTypo]}>
          Nasser 11/20 9:31 Win 134309
        </Text>
        <ImageBackground
          style={[styles.image13Icon, styles.iconLayout]}
          resizeMode="cover"
          source={require("../assets/image1.png")}
        />
        <Text style={[styles.abdullah1120522, styles.abdulqadirTypo]}>
          Abdullah 11/20 5:22 Lose 134308
        </Text>
        <ImageBackground
          style={[styles.image14Icon, styles.iconLayout]}
          resizeMode="cover"
          source={require("../assets/image1.png")}
        />
        <Text style={[styles.hassan1120423, styles.abdulqadirTypo]}>
          Hassan 11/20 4:23 Win 134307
        </Text>
        <ImageBackground
          style={[styles.image15Icon, styles.iconLayout]}
          resizeMode="cover"
          source={require("../assets/image1.png")}
        />
        <Text style={[styles.raad1120334, styles.abdulqadirTypo]}>
          Raad 11/20 3:34 Lose 134306
        </Text>
        <ImageBackground
          style={[styles.image16Icon, styles.iconLayout]}
          resizeMode="cover"
          source={require("../assets/image1.png")}
        />
        <Text style={[styles.yosef1120845, styles.abdulqadirTypo]}>
          Yosef 11/20 8:45 Lose 134305
        </Text>
        <ImageBackground
          style={[styles.image17Icon, styles.iconLayout]}
          resizeMode="cover"
          source={require("../assets/image1.png")}
        />
        <Text style={[styles.abdulqadir1124655, styles.abdulqadirTypo]}>
          Abdulqadir 11/24 6:55 Win 134321
        </Text>
        <ImageBackground
          style={[styles.image18Icon, styles.iconLayout]}
          resizeMode="cover"
          source={require("../assets/image1.png")}
        />
      </ScrollView>
      <Text style={[styles.records1, styles.pgnFlexBox]}>Records</Text>
      <Button
        style={styles.image20}
        mode="text"
        onPress={() => navigation.navigate("Home")}
        contentStyle={styles.image20IconBtn}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  image20IconBtn: {
    height: 30,
    width: 30,
  },
  pgnFlexBox: {
    textAlign: "left",
    color: Color.colorWhite,
    position: "absolute",
  },
  abdulqadirTypo: {
    left: 0,
    textAlign: "left",
    color: Color.colorWhite,
    fontFamily: FontFamily.interLight,
    fontWeight: "300",
    fontSize: FontSize.size_smi,
    position: "absolute",
  },
  iconLayout: {
    height: 26,
    width: 28,
    left: 340,
    position: "absolute",
  },
  dallE20231030213013IIcon: {
    top: 25,
    left: 75,
    width: 279,
    height: 189,
    position: "absolute",
  },
  recordsChild: {
    top: 285,
    left: 8,
    width: 415,
    height: 29,
    position: "absolute",
  },
  player: {
    left: 38,
    fontFamily: FontFamily.interLight,
    fontWeight: "300",
    fontSize: FontSize.size_smi,
    top: 291,
    color: Color.colorWhite,
  },
  date: {
    left: 101,
    fontFamily: FontFamily.interLight,
    fontWeight: "300",
    fontSize: FontSize.size_smi,
    top: 291,
    color: Color.colorWhite,
  },
  duration: {
    left: 153,
    fontFamily: FontFamily.interLight,
    fontWeight: "300",
    fontSize: FontSize.size_smi,
    top: 291,
    color: Color.colorWhite,
  },
  result: {
    left: 228,
    fontFamily: FontFamily.interLight,
    fontWeight: "300",
    fontSize: FontSize.size_smi,
    top: 291,
    color: Color.colorWhite,
  },
  pgn: {
    left: 364,
    fontFamily: FontFamily.interLight,
    fontWeight: "300",
    fontSize: FontSize.size_smi,
    top: 291,
    color: Color.colorWhite,
  },
  matchid: {
    left: 288,
    fontFamily: FontFamily.interLight,
    fontWeight: "300",
    fontSize: FontSize.size_smi,
    top: 291,
    color: Color.colorWhite,
  },
  abdulqadir1124414: {
    top: 5,
  },
  image1Icon: {
    top: 0,
  },
  wadie1124614: {
    top: 42,
  },
  image2Icon: {
    top: 37,
  },
  abdulaziz1123732: {
    top: 79,
  },
  image3Icon: {
    top: 74,
  },
  ahmed1123444: {
    top: 116,
  },
  image4Icon: {
    top: 111,
  },
  rakan1122635: {
    top: 153,
  },
  image5Icon: {
    top: 148,
  },
  waleed1122918: {
    top: 190,
  },
  image6Icon: {
    top: 185,
  },
  faisal1122817: {
    top: 227,
  },
  image7Icon: {
    top: 222,
  },
  ibrahim1121735: {
    top: 264,
  },
  image8Icon: {
    top: 259,
  },
  saad1121451: {
    top: 301,
  },
  image9Icon: {
    top: 296,
  },
  shaker1121334: {
    top: 338,
  },
  image10Icon: {
    top: 333,
  },
  hussain1121912: {
    top: 375,
  },
  image11Icon: {
    top: 370,
  },
  ali1121842: {
    top: 412,
  },
  image12Icon: {
    top: 407,
  },
  nasser1120931: {
    top: 449,
  },
  image13Icon: {
    top: 444,
  },
  abdullah1120522: {
    top: 486,
  },
  image14Icon: {
    top: 481,
  },
  hassan1120423: {
    top: 523,
  },
  image15Icon: {
    top: 518,
  },
  raad1120334: {
    top: 560,
  },
  image16Icon: {
    top: 555,
  },
  yosef1120845: {
    top: 597,
  },
  image17Icon: {
    top: 592,
  },
  abdulqadir1124655: {
    top: 634,
  },
  image18Icon: {
    top: 629,
  },
  recordData: {
    top: 320,
    left: 24,
    width: 368,
    maxWidth: 368,
    position: "absolute",
    flex: 1,
  },
  records1: {
    top: 214,
    left: 145,
    fontSize: FontSize.size_16xl,
    fontWeight: "600",
    fontFamily: FontFamily.interSemiBold,
  },
  image20: {
    top: 69,
    left: 21,
    position: "absolute",
  },
  records: {
    backgroundColor: Color.colorGray_100,
    width: "100%",
    height: 932,
    overflow: "hidden",
    flex: 1,
  },
});

export default Records;
