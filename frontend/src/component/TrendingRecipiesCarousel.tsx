import { Carousel } from "@mantine/carousel";
import {
  DaCard,
  DaCard2,
  DaCard3,
  DaCard4,
} from "../component/TrendingRecipiesCard";
import { Card, Title, createStyles, rem } from "@mantine/core";

const useStyles = createStyles((theme) => ({
  cardWrapper: {
    display: "flex",
    width: "90%",
    position: "absolute",
    left: "8%",
  },
  card: {
    background: "#fff",
    borderRadius: "15px",
    boxShadow:
      "0 0.0625rem 0.1875rem rgba(0, 0, 0, 0.05), rgba(0, 0, 0, 0.05) 0 0.625rem 0.9375rem -0.3125rem, rgba(0, 0, 0, 0.04) 0 0.4375rem 0.4375rem -0.3125rem",
    display: "inline-block",
    padding: "30px 35px",
    perspective: "1800px",
    textAlign: "left",
    transformOrigin: "50% 50%",
    transformStyle: "preserve-3d",
    minWidth: "595px",
    width: "90%",
    height: "500px",
    transition:"1s",
    '&:hover': {
      boxShadow: "0px 10px 20px 20px rgba(0, 0, 0, 0.17)",
    }
  },
  titles: {
    color: "#3e3e42",
    fontSize: "32px",
    fontWeight: 800,
    letterSpacing: "-1px",
  },
  title: {
    color: "#228be6",
    fontSize: "16px",
  },
}));
export function DaCarousel() {
  const { classes } = useStyles();
  return (
    <div className={classes.card}>
      <Title order={5} className={classes.title}>Recipes</Title>
      <Title order={1} className={classes.titles} >Trending</Title>
      <Carousel
        className={classes.cardWrapper}
        withIndicators
        height={350}
        slideSize="33.333333%"
        slideGap="sm"
        loop
        align="start"
        breakpoints={[
          { maxWidth: "md", slideSize: "50%" },
          { maxWidth: "sm", slideSize: "100%", slideGap: 0 },
        ]}
        mt={10}
      >
        <Carousel.Slide>
          {" "}
          <DaCard />
        </Carousel.Slide>
        <Carousel.Slide>
          {" "}
          <DaCard2 />
        </Carousel.Slide>
        <Carousel.Slide>
          {" "}
          <DaCard3 />
        </Carousel.Slide>
        <Carousel.Slide>
          {" "}
          <DaCard4 />
        </Carousel.Slide>
      </Carousel>
    </div>
  );
}
