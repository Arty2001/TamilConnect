import {
  Avatar,
  Container,
  Center,
  Group,
  Pagination,
  Select,
  Stack,
  Text,
  Grid,
  AspectRatio,
  List,
  Title,
  ThemeIcon,
  Card,
  createStyles,
  Image,
} from "@mantine/core";
import { RecipeCard } from "../component/RecipeCard";

import { useSearchParams } from "react-router-dom";
import { forwardRef, useEffect, useState } from "react";
import { ceil } from "mathjs";
import {
  IconBorderRadius,
  IconChevronDown,
  IconCircle,
  IconCircleCheck,
  IconCircleDashed,
  IconCircleX,
} from "@tabler/icons-react";

const useStyles = createStyles((theme) => ({
  largeContainer: {
    //boxShadow: "5px 5px 10px 10px",
    borderStyle: "solid",
    margin: "2.5em",
    borderRadius: "3em",
  },

  container: {
    //display: "flex",
    //flexDirection: "column",
    color: "black",
    marginLeft: "1em",
    marginRight: "1em",
    maxWidth: "100%",
  },
  grid: {},

  title: {
    alignSelf: "baseline",
    marginTop: "1em",
  },
  author: {
    alignSelf: "baseline",
  },
  pillFacts: {
    display: "flex",
    flexDirection: "row",
    marginLeft: "1em",
    marginTop: "20px",
    gap: "10px",
  },
  pillFact: {
    backgroundColor: "",
    border: "solid",
    borderWidth: "thick",
    borderColor: "#e7f5ff",
    color: "black",
    padding: "0.3em 0.5em",
    //display: "inline-block",
    fontSize: "14px",
    margin: "4px 2px",
    borderRadius: "20px",
  },
  time: {
    marginLeft: "1em",
    display: "flex",
    flexDirection: "row",
    marginTop: "0px",
    gap: "15px",
  },

  subTime: {},
  hr: {
    height: "2px",
    width: "100%",
    borderWidth: "1",
    color: "black",
    backgroundColor: "black",
  },
  nutritionalFacts: {
    marginLeft: "1em",
    display: "flex",
    flexDirection: "row",
    gap: "15px",
  },
  nutritionPerServingNumber: {
    color: "black",
  },
  nutritionPerServingText: {
    marginTop: "0.5em",
    alignSelf: "center",
  },
  nutritionItem: {
    display: "flex",
    flexDirection: "column",
    backgroundColor: "#e7f5ff",

    color: "black",
    padding: "0.5em 0.7em",
    fontSize: "14px",
    margin: "4px 2px",
    height: "8em",
    borderRadius: "35px",
  },

  foodImage: {
    marginBottom: "3em",
    marginTop: "3em",
  },
  instructionNumbers: {
    color: "black",
  },
  ingredientsCard: {
    backgroundColor: "#e7f5ff",
    height: "30em",
  },
  videoTutorial: {
    marginBottom: "1em",
    marginTop: "1em",
  },
}));
export function Recipes() {
  const [searchParams, setSearchParams] = useSearchParams();
  const [mockData, setMockData] = useState([]);
  const { classes } = useStyles();

  useEffect(() => {
    fetch("http://localhost:5000/api/GetRecipes")
      .then((response) => response.json())
      .then((data) => setMockData(data));
  }, []);

  interface ItemProps extends React.ComponentPropsWithoutRef<"div"> {
    imagesource: string;
    name: string;
    value: string;
    description: string;
    rating: string;
    author: {
      name: string;
      image: string;
    };
  }

  const [activePage, setPage] = useState(1);

  const SelectItem = forwardRef<HTMLDivElement, ItemProps>(
    ({ imagesource, name, description, ...others }: ItemProps, ref) => (
      <div ref={ref}>
        <Group noWrap {...others}>
          <Avatar
            src={imagesource}
            onClick={() => {
              setSearchParams({ recipe: name });
            }}
          />

          <div>
            <Text size="sm">{name}</Text>
            <Text size="xs" lineClamp={3} opacity={0.65}>
              {description}
            </Text>
          </div>
        </Group>
      </div>
    )
  );

  const chunkSize = 6;
  console.log(searchParams.get("recipe"));
  if (
    searchParams.get("recipe") === null ||
    searchParams.get("recipe") === ""
  ) {
    return (
      <Container size="xl" px={0}>
        <Stack justify="center" spacing="xl">
          <Center>
            <Select
              label="Search A Recipe"
              placeholder="Pick one"
              itemComponent={SelectItem}
              data={mockData}
              searchable
              size="sm"
              onChange={(item: string) => {
                setSearchParams({ recipe: item });
              }}
              maxDropdownHeight={400}
              nothingFound="No Recipes Found"
              filter={(value, item) =>
                item.name.toLowerCase().includes(value.toLowerCase().trim()) ||
                item.description
                  .toLowerCase()
                  .includes(value.toLowerCase().trim())
              }
              sx={{ width: 800 }}
              transitionProps={{
                transition: "pop-top-left",
                duration: 80,
                timingFunction: "ease",
              }}
              rightSection={<IconChevronDown size="1rem" />}
              rightSectionWidth={30}
            />
          </Center>
          <Group position="center">
            {mockData
              .slice(
                (activePage - 1) * chunkSize,
                (activePage - 1) * chunkSize + chunkSize
              )
              .map((recipe: any, i: any) => {
                return (
                  <RecipeCard
                    key={i}
                    title={recipe.name}
                    author={recipe.author}
                    description={recipe.description}
                    rating={recipe.rating}
                    image={recipe.imagesource}
                    onClick={() => {
                      setSearchParams({ recipe: recipe.name });
                    }}
                  />
                );
              })}
          </Group>
          <Center>
            <Pagination
              total={ceil(mockData.length / chunkSize)}
              defaultValue={1}
              onChange={setPage}
            />
          </Center>
        </Stack>
      </Container>
    );
  } else {
    let oatsIdliIngredients = [
      "2 cups of oats",
      "1 cup of curd",
      "A pinch of baking soda",
      "Salt to taste",
      "1 carrot, grated",
      "Some chopped coriander leaves",
      "1 tablespoon oil",
      "1 teaspoon mustard seeds",
      "Some curry leaves",
      "1 teaspoon urad dal",
      "1 teaspoon chana dal",
    ];

    let oatsIdliSteps = [
      "Roast the oats in a pan till they turn slightly brown and then powder the oats in a mixer.",
      "In a pan, add some oil and temper the mustard seeds, curry leaves, urad dal, and chana dal.",
      "Add the grated carrot and chopped coriander to the pan and sauté them.",
      "Add this to the powdered oats in a bowl.",
      "Add salt, curd, and a pinch of baking soda to the bowl and mix well. If required, add some water so that the batter gets the consistency of an idli batter.",
      "Grease the idli moulds with some oil and pour the batter into the idli plates.",
      "Steam in a cooker or steamer for about 15 minutes.",
      "Serve the oats idli hot with some coconut chutney.",
    ];

    return (
      <div className={classes.largeContainer}>
        <Center className={classes.title}>
          <Title order={1}>{searchParams.get("recipe")}</Title>
        </Center>
        <Center className={classes.author}>
          <Title order={5}>By Dhana Rameshan</Title>
        </Center>
        <Container size="xl" px={0} className={classes.container}>
          <Grid columns={24} className={classes.grid}>
            <Grid.Col span={16}>
              <>
                <div className={classes.pillFacts}>
                  <div className={classes.pillFact}>
                    {" "}
                    <span role="img" aria-label="leaf">
                      🍃
                    </span>{" "}
                    Vegetarian{" "}
                  </div>
                  <div className={classes.pillFact}>
                    <span role="img" aria-label="plate and knifer">
                      🍽
                    </span>{" "}
                    Low Fat{" "}
                  </div>
                  <div className={classes.pillFact}>
                    <span role="img" aria-label="chicken leg">
                      🍗
                    </span>{" "}
                    High Fiber{" "}
                  </div>
                </div>
                <div className={classes.time}>
                  <div className={classes.subTime}> Prep: 25 mins </div>
                  <div className={classes.subTime}> Cook: 15 mins</div>
                  <div className={classes.subTime}> Total: 40 mins</div>
                </div>
                <hr className={classes.hr}></hr>
                <div>Nutrition Per Serving</div>
                <div className={classes.nutritionalFacts}>
                  <div className={classes.nutritionItem}>
                    <ThemeIcon color="white" size={56} radius="xl">
                      {" "}
                      <div className={classes.nutritionPerServingNumber}>
                        255
                      </div>
                    </ThemeIcon>
                    <div className={classes.nutritionPerServingText}>
                      Calories
                    </div>
                  </div>

                  <div className={classes.nutritionItem}>
                    <ThemeIcon color="white" size={56} radius="xl">
                      {" "}
                      <div className={classes.nutritionPerServingNumber}>
                        2 g
                      </div>
                    </ThemeIcon>
                    <div className={classes.nutritionPerServingText}>Carbs</div>
                  </div>
                  <div className={classes.nutritionItem}>
                    <ThemeIcon color="white" size={56} radius="xl">
                      {" "}
                      <div className={classes.nutritionPerServingNumber}>
                        2 g
                      </div>
                    </ThemeIcon>
                    <div className={classes.nutritionPerServingText}>Fat</div>
                  </div>
                  <div className={classes.nutritionItem}>
                    <ThemeIcon color="white" size={56} radius="xl">
                      {" "}
                      <div className={classes.nutritionPerServingNumber}>
                        9 g
                      </div>
                    </ThemeIcon>
                    <div className={classes.nutritionPerServingText}>
                      Protein
                    </div>
                  </div>
                  <div className={classes.nutritionItem}>
                    <ThemeIcon color="white" size={56} radius="xl">
                      {" "}
                      <div className={classes.nutritionPerServingNumber}>
                        1 g
                      </div>
                    </ThemeIcon>
                    <div className={classes.nutritionPerServingText}>Sugar</div>
                  </div>
                </div>
                <hr className={classes.hr}></hr>
                <Title order={3}>Instructions</Title>
                <List spacing="xs" size="sm" center>
                  {oatsIdliSteps.map((instruction, index) => {
                    return (
                      <List.Item
                        icon={
                          <ThemeIcon color="#e7f5ff" size={32} radius="xl">
                            <div className={classes.instructionNumbers}>
                              {" "}
                              {index + 1}
                            </div>
                          </ThemeIcon>
                        }
                      >
                        {instruction}
                      </List.Item>
                    );
                  })}
                </List>

                <div className={classes.videoTutorial}>
                  <Title order={3}>Tutorial</Title>

                  <AspectRatio ratio={1080 / 620}>
                    <iframe
                      src="https://www.youtube.com/embed/Dorf8i6lCuk"
                      title="YouTube video player"
                      frameBorder="0"
                      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                      allowFullScreen
                    />
                  </AspectRatio>
                </div>
              </>
            </Grid.Col>
            <Grid.Col span={8}>
              <Image
                maw={500}
                mx="auto"
                radius="md"
                src="https://www.vegrecipesofindia.com/wp-content/uploads/2019/01/oats-idli-recipe-1.jpg"
                alt="Food Item"
                className={classes.foodImage}
              />

              <Stack>
                <Card
                  className={classes.ingredientsCard}
                  shadow="sm"
                  padding="lg"
                  radius="md"
                  withBorder
                  color="#e7f5ff"
                >
                  <Center mb={10}>
                    <Title order={3}>Ingredients</Title>
                  </Center>
                  <List
                    spacing="md"
                    size="sm"
                    center
                    icon={
                      <ThemeIcon color="black" size={9} radius="xl">
                        <></>
                      </ThemeIcon>
                    }
                  >
                    {oatsIdliIngredients.map((ingredient) => {
                      return <List.Item>{ingredient}</List.Item>;
                    })}
                  </List>
                </Card>
              </Stack>
            </Grid.Col>
          </Grid>
        </Container>
      </div>
    );
  }
}
