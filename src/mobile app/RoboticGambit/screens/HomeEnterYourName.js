import * as React from "react";
import {
  ImageBackground,
  StyleSheet,
  Text,
  TextInput,
  View,
} from "react-native";
import { Button } from "react-native-paper";
import { useNavigation } from "@react-navigation/native";
import { FontSize, Color, FontFamily, Border, Padding } from "../GlobalStyles";

const HomeEnterYourName = () => {
  const navigation = useNavigation();

  return (
    <View style={styles.homeEnterYourName}>
      <ImageBackground
        style={styles.dallE20231030213013IIcon}
        resizeMode="cover"
        source={require("../assets/dalle20231030213013illustrationofastreamlinedlogoforroboticgambit11.png")}
      />
      <Button
        style={styles.image19}
        mode="text"
        onPress={() => navigation.goBack()}
        contentStyle={styles.image19IconBtn}
      />
      <Text style={[styles.startMatch, styles.startMatchFlexBox]}>
        Start Match
      </Text>
      <Text style={[styles.trainYourselfBy, styles.startMatchFlexBox]}>
        Train yourself by defeating yourself !
      </Text>
      <TextInput
        style={[styles.homeEnterYourNameChild, styles.homeShadowBox]}
        placeholder="Enter your name"
        placeholderTextColor="rgba(0, 0, 0, 0.32)"
      />
      <Button
        style={[styles.homeEnterYourNameItem, styles.homeShadowBox]}
        mode="text"
        labelStyle={styles.frameButtonBtn}
        onPress={() => navigation.navigate("MatchSenario")}
        contentStyle={styles.frameButtonBtn1}
      >
        Start
      </Button>
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
  startMatchFlexBox: {
    textAlign: "left",
    position: "absolute",
  },
  homeShadowBox: {
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
  dallE20231030213013IIcon: {
    top: 25,
    height: 189,
    width: 279,
    left: 75,
    position: "absolute",
  },
  image19: {
    top: 69,
    left: 21,
    position: "absolute",
  },
  startMatch: {
    top: 214,
    left: 115,
    fontSize: FontSize.size_16xl,
    color: Color.colorWhite,
    fontFamily: FontFamily.interSemiBold,
    fontWeight: "600",
  },
  trainYourselfBy: {
    top: 371,
    left: 77,
    fontFamily: FontFamily.interRegular,
    color: Color.colorGray_400,
    fontSize: FontSize.size_base,
  },
  homeEnterYourNameChild: {
    top: 510,
    borderRadius: Border.br_8xs,
    backgroundColor: Color.colorGray_300,
    height: 39,
    padding: Padding.p_3xs,
    fontSize: FontSize.size_base,
    fontFamily: FontFamily.interSemiBold,
    fontWeight: "600",
    width: 279,
  },
  homeEnterYourNameItem: {
    top: 595,
  },
  homeEnterYourName: {
    backgroundColor: Color.colorGray_100,
    flex: 1,
    width: "100%",
    height: 932,
    overflow: "hidden",
  },
});

export default HomeEnterYourName;
