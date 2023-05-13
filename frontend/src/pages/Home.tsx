import { useState, useEffect } from "react";
import { HeroTitle } from "../component/WelcomeBack";
import { DaCard } from "../component/TrendingRecipiesCard";
import { DaCarousel } from "../component/TrendingRecipiesCarousel";
//import { ArticleCards } from "../component/temp";
import { ArticleCard } from "../component/GroceryItemCard";
import { AddItemsContainer } from "../component/GroceryAddItems";
import { InCartCard } from "../component/InCartCard";
import { Cart } from "../component/Cart";
import { createStyles } from "@mantine/core";

const useStyles = createStyles((theme) => ({
  homePage: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  },
  AddItemsContainer: {
    marginTop: "40em", //this is temp to be able to see them all
  },

  Carousel: {
    marginTop: "1em",
  },
}));

export function Home() {
  const [resto, setResto] = useState();
  const { classes } = useStyles();

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
  return (
    <>
      <div className={classes.homePage}>
        <HeroTitle />

        {/* <p>{resto}</p> removed this idk what it does */}
        <div className={classes.Carousel}>
          <DaCarousel />
        </div>

        <div className={classes.AddItemsContainer}>
          <AddItemsContainer />
        </div>
        <Cart />
      </div>
    </>
  );
}
