import * as React from "react";
import { ImageBackground, StyleSheet, Text, View } from "react-native";
import { Button } from "react-native-paper";
import { useNavigation } from "@react-navigation/native";
import { FontSize, FontFamily, Color } from "../GlobalStyles";

const Home = () => {
  const navigation = useNavigation();

  return (
    <View style={styles.home}>
      <ImageBackground
        style={styles.dallE20231030213013IIcon}
        resizeMode="cover"
        source={require("../assets/dalle20231030213013illustrationofastreamlinedlogoforroboticgambit1.png")}
      />
      <Button
        style={[styles.homeChild, styles.homeShadowBox]}
        disabled={false}
        uppercase={false}
        mode="text"
        labelStyle={styles.frameButtonBtn}
        onPress={() => navigation.navigate("HomeEnterYourName")}
        contentStyle={styles.frameButtonBtn1}
      >
        Start Match
      </Button>
      <Button
        style={[styles.homeItem, styles.homeShadowBox]}
        mode="text"
        labelStyle={styles.frameButton1Btn}
        onPress={() => navigation.navigate("Records")}
        contentStyle={styles.frameButton1Btn1}
      >
        See Records
      </Button>
      <Text style={styles.trainYourselfBy}>
        Train yourself by defeating yourself !
      </Text>
    </View>
  );
};

const styles = StyleSheet.create({
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
  frameButton1Btn: {
    color: "#fff",
    fontSize: 16,
    fontWeight: "600",
    fontFamily: "Inter-SemiBold",
  },
  frameButton1Btn1: {
    padding: 10,
    borderRadius: 5,
    height: 39,
    width: 279,
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
    top: 92,
    width: 279,
    height: 265,
    left: 75,
    position: "absolute",
  },
  homeChild: {
    top: 510,
  },
  homeItem: {
    top: 595,
  },
  trainYourselfBy: {
    top: 372,
    left: 78,
    fontSize: FontSize.size_base,
    fontFamily: FontFamily.interRegular,
    color: Color.colorGray_400,
    textAlign: "left",
    position: "absolute",
  },
  home: {
    backgroundColor: Color.colorGray_100,
    flex: 1,
    width: "100%",
    height: 932,
    overflow: "hidden",
  },
});

export default Home;
