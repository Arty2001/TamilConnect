import { useState, useEffect } from "react";
import { HeroTitle } from "../component/WelcomeBack";
import { DaCard } from "../component/TrendingRecipiesCard";
import { DaCarousel } from "../component/TrendingRecipiesCarousel";
//import { ArticleCards } from "../component/temp";
import { ArticleCard } from "../component/GroceryItemCard";
import { AddItemsContainer } from "../component/GroceryAddItems";
import { ModalGrocery } from "../component/ModalGrocery";
import { InCartCard } from "../component/InCartCard";
import { Cart } from "../component/Cart";
import { createStyles } from "@mantine/core";
import { useMediaQuery } from "@mantine/hooks";

const useStyles = createStyles((theme) => ({
  homePage: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    height: "100%",
  },
  Welcome: {
    //width: "100%",
    //position: "absolute",
    marginLeft: "0px",
    marginRight: "0px",
    flexBasis: "100%",
  },
  homePageMobile: {
    display: "flex",
    flexDirection: "column",
    alignItems: "left",
  },

  Carousel: {
    marginTop: "1em",
  },

  ModalGrocery: {
    marginTop: "30em",
  },
}));

export function Home() {
  const [resto, setResto] = useState();
  const { classes } = useStyles();

  const desktop = useMediaQuery("(min-width: 56.25em)");

  useEffect(() => {
    const fetchResto = async () => {
      const response = await fetch(
        "http://172.20.10.2:5000/api/FindResto?grocery=chicken&location=montreal"
      );
      const data = await response.json(); //json is the data shared among all
      setResto(data);
    };
    fetchResto();
  }, [resto]);

  {
    /* if (!mobile) {
    return <div> hel</div>;
  }
*/
  }
  return (
    <>
      <div className={desktop ? classes.homePage : classes.homePageMobile}>
        <div className={classes.Welcome}>
          <HeroTitle />
        </div>

        {/* <p>{resto}</p> removed this idk what it does */}
        <div className={classes.Carousel}>
          <DaCarousel />
        </div>
        <div className={classes.ModalGrocery}>
          <ModalGrocery />
        </div>
      </div>
    </>
  );
}
