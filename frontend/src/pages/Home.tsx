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
import { Stack, createStyles } from "@mantine/core";
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
  const { classes } = useStyles();

  const desktop = useMediaQuery("(min-width: 56.25em)");
  
  return (
    <Stack spacing="lg" justify="center" align="center">
          <HeroTitle />
          <DaCarousel />
          <ModalGrocery />
    </Stack>
  );
}
