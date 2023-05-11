import { useState, useEffect } from "react";
import { HeroTitle } from "../component/WelcomeBack";
import { DaCard } from "../component/TrendingRecipiesCard";
import { DaCarousel } from "../component/TrendingRecipiesCarousel";
import { ArticleCards } from "../component/GroceryItemCard";
import { createStyles } from "@mantine/core";

const useStyles = createStyles((theme) => ({
  homePage: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  },
}));

export function Home() {
  const [resto, setResto] = useState();

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
      <div className="homePage">
        <HeroTitle />

        {/* <p>{resto}</p> removed this idk what it does */}

        <DaCarousel />
      </div>
      <div>
        {" "}
        <ArticleCards />
      </div>
    </>
  );
}
