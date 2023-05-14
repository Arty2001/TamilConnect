import { Carousel } from "@mantine/carousel";
import {
  DaCard,
  DaCard2,
  DaCard3,
  DaCard4,
} from "../component/TrendingRecipiesCard";
import { createStyles, rem } from "@mantine/core";

const useStyles = createStyles((theme) => ({
  cardWrapper: {
    display: "flex",
    width: "80%",
    position: "absolute",
    left: "8%",
  },
}));
export function DaCarousel() {
  const { classes } = useStyles();
  return (
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
  );
}
