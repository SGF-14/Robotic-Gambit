import * as React from "react";
import {
  ImageBackground,
  StyleSheet,
  Text,
  View,
  Pressable,
} from "react-native";
import { Button } from "react-native-paper";
import { Image } from "expo-image";
import { useNavigation } from "@react-navigation/native";
import { Padding, Color, Border, FontFamily, FontSize } from "../GlobalStyles";

const MatchSenario18Result = () => {
  const navigation = useNavigation();

  return (
    <View style={styles.matchSenario18Result}>
      <ImageBackground
        style={styles.dallE20231030213013IIcon}
        resizeMode="cover"
        source={require("../assets/dalle20231030213013illustrationofastreamlinedlogoforroboticgambit11.png")}
      />
      <Button
        style={styles.image19}
        mode="text"
        onPress={() => navigation.navigate("Home")}
        contentStyle={styles.image19IconBtn}
      />
      <Image
        style={styles.frameIcon}
        contentFit="cover"
        source={require("../assets/frame1.png")}
      />
      <Text style={styles.match}>Match</Text>
      <Pressable
        style={[styles.wrapper, styles.wrapperShadowBox]}
        onPress={() => navigation.navigate("HomeEnterYourName")}
      >
        <Text style={styles.text}>9:38</Text>
      </Pressable>
      <Pressable
        style={[styles.container, styles.wrapperShadowBox]}
        onPress={() => navigation.navigate("HomeEnterYourName")}
      >
        <Text style={styles.text}>9:48</Text>
      </Pressable>
      <Text style={[styles.abdulqadir, styles.abdulqadirTypo]}>Abdulqadir</Text>
      <Text style={[styles.roboticGambit, styles.abdulqadirTypo]}>
        Robotic Gambit
      </Text>
      <Button
        style={styles.matchSenario18ResultChild}
        mode="text"
        labelStyle={styles.frameButtonBtn}
        onPress={() => navigation.navigate("Home")}
        contentStyle={styles.frameButtonBtn1}
      >
        Surrender
      </Button>
      <Image
        style={styles.component1Icon}
        contentFit="cover"
        source={require("../assets/component-1.png")}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  image19IconBtn: {
    height: 30,
    width: 30,
  },
  frameButtonBtn: {
    color: "#fff",
    fontSize: 16,
    fontWeight: "600",
    fontFamily: "Inter-SemiBold",
  },
  frameButtonBtn1: {
    padding: 10,
    borderRadius: 5,
    height: 39,
    width: 279,
  },
  wrapperShadowBox: {
    padding: Padding.p_3xs,
    height: 29,
    width: 69,
    backgroundColor: Color.colorGray_300,
    borderRadius: Border.br_8xs,
    left: 321,
    justifyContent: "center",
    alignItems: "center",
    flexDirection: "row",
    shadowOpacity: 1,
    elevation: 50,
    shadowRadius: 50,
    shadowOffset: {
      width: 0,
      height: 10,
    },
    shadowColor: "rgba(0, 0, 0, 0.15)",
    position: "absolute",
  },
  abdulqadirTypo: {
    color: Color.colorGray_400,
    fontFamily: FontFamily.interRegular,
    fontSize: FontSize.size_base,
    textAlign: "left",
    position: "absolute",
  },
  dallE20231030213013IIcon: {
    top: 25,
    width: 279,
    height: 189,
    left: 75,
    position: "absolute",
  },
  image19: {
    top: 69,
    left: 21,
    position: "absolute",
  },
  frameIcon: {
    top: 334,
    left: 34,
    width: 363,
    height: 352,
    position: "absolute",
    overflow: "hidden",
  },
  match: {
    top: 214,
    left: 161,
    fontSize: FontSize.size_16xl,
    color: Color.colorWhite,
    textAlign: "left",
    fontFamily: FontFamily.interSemiBold,
    fontWeight: "600",
    position: "absolute",
  },
  text: {
    color: Color.colorGray_200,
    fontSize: FontSize.size_base,
    textAlign: "left",
    fontFamily: FontFamily.interSemiBold,
    fontWeight: "600",
  },
  wrapper: {
    top: 300,
  },
  container: {
    top: 692,
  },
  abdulqadir: {
    top: 696,
    left: 42,
  },
  roboticGambit: {
    top: 305,
    left: 41,
  },
  matchSenario18ResultChild: {
    top: 799,
    justifyContent: "center",
    alignItems: "center",
    flexDirection: "row",
    shadowOpacity: 1,
    elevation: 50,
    shadowRadius: 50,
    shadowOffset: {
      width: 0,
      height: 10,
    },
    shadowColor: "rgba(0, 0, 0, 0.15)",
    left: 75,
    position: "absolute",
  },
  component1Icon: {
    top: 390,
    left: 53,
    width: 326,
    height: 373,
    position: "absolute",
  },
  matchSenario18Result: {
    backgroundColor: Color.colorGray_100,
    flex: 1,
    width: "100%",
    height: 932,
    overflow: "hidden",
  },
});

export default MatchSenario18Result;
