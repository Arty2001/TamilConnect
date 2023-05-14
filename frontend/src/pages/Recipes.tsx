import { Avatar, Container, Center, Group, Pagination, Select, Stack, Text, Grid, AspectRatio, List, Title, ThemeIcon, Card } from "@mantine/core"
import { RecipeCard } from "../component/RecipeCard"

import { useSearchParams } from 'react-router-dom';
import { forwardRef, useEffect, useState } from "react";
import { ceil } from 'mathjs';
import { IconChevronDown, IconCircleCheck, IconCircleDashed, IconCircleX } from "@tabler/icons-react";


export function Recipes() {
    const [searchParams, setSearchParams] = useSearchParams();
    const [mockData, setMockData] = useState([]);

    useEffect( () => { 
        fetch("http://10.0.0.142:5000/api/GetRecipes")
            .then(response => response.json())
            .then(data => setMockData(data));

    } , [])

    interface ItemProps extends React.ComponentPropsWithoutRef<'div'> {
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
                    <Avatar src={imagesource} onClick={() => { setSearchParams({ recipe: name }); }} />

                    <div >
                        <Text size="sm" >{name}</Text>
                        <Text size="xs" lineClamp={3} opacity={0.65}>
                            {description}
                        </Text>
                    </div>
                </Group>
            </div>
        )
    );


    const chunkSize = 6
    console.log(searchParams.get("recipe"))
    if (searchParams.get("recipe") === null || searchParams.get("recipe") === "") {
        return (
            <Container size="xl" px={0}><Stack justify="center" spacing="xl">
                <Center>
                    <Select
                        label="Search A Recipe"
                        placeholder="Pick one"
                        itemComponent={SelectItem}
                        data={mockData}
                        searchable
                        size="sm"
                        onChange={(item: string) => { setSearchParams({ recipe: item }) }}
                        maxDropdownHeight={400}
                        nothingFound="No Recipes Found"
                        filter={(value, item) => item.name.toLowerCase().includes(value.toLowerCase().trim()) ||
                            item.description.toLowerCase().includes(value.toLowerCase().trim())}
                        sx={{ width: 800 }}
                        transitionProps={{ transition: 'pop-top-left', duration: 80, timingFunction: 'ease' }}
                        rightSection={<IconChevronDown size="1rem" />}
                        rightSectionWidth={30}
                    />
                </Center>
                <Group position="center">
                    {mockData.slice((activePage - 1) * chunkSize, (activePage - 1) * chunkSize + chunkSize).map((recipe: any, i: any) => {
                        return (
                            <RecipeCard
                                key={i}
                                title={recipe.name}
                                author={recipe.author}
                                description={recipe.description}
                                rating={recipe.rating}
                                image={recipe.imagesource}
                                onClick={() => { setSearchParams({ recipe: recipe.name }); }} />
                        );
                    })}
                </Group>
                <Center>
                    <Pagination total={ceil(mockData.length / chunkSize)} defaultValue={1} onChange={setPage} />
                </Center>
            </Stack>
            </Container>
        )
    }
    else {
        let oatsIdliIngredients = [
            '2 cups of oats',
            '1 cup of curd',
            'A pinch of baking soda',
            'Salt to taste',
            '1 carrot, grated',
            'Some chopped coriander leaves',
            '1 tablespoon oil',
            '1 teaspoon mustard seeds',
            'Some curry leaves',
            '1 teaspoon urad dal',
            '1 teaspoon chana dal'
        ];

        let oatsIdliSteps = [
            'Roast the oats in a pan till they turn slightly brown and then powder the oats in a mixer.',
            'In a pan, add some oil and temper the mustard seeds, curry leaves, urad dal, and chana dal.',
            'Add the grated carrot and chopped coriander to the pan and sauté them.',
            'Add this to the powdered oats in a bowl.',
            'Add salt, curd, and a pinch of baking soda to the bowl and mix well. If required, add some water so that the batter gets the consistency of an idli batter.',
            'Grease the idli moulds with some oil and pour the batter into the idli plates.',
            'Steam in a cooker or steamer for about 15 minutes.',
            'Serve the oats idli hot with some coconut chutney.'
        ];

        return (
            <Container size="xl" px={0}>
                <Center><Title order={1}>{searchParams.get("recipe")}</Title></Center>
                <Center><Title order={5}>By Dhana Rameshan</Title></Center>
                <Grid columns={24}>
                    <Grid.Col span={16}><><Title order={3}>Instructions</Title>
                        <List
                            spacing="xs"
                            size="sm"
                            center
                        >
                            {oatsIdliSteps.map((instruction) => {
                                return <List.Item
                                    icon={
                                        <ThemeIcon color="red" size={24} radius="xl">
                                            <IconCircleX size="1rem" />
                                        </ThemeIcon>
                                    }
                                >
                                    {instruction}
                                </List.Item>
                            })}
                        </List>

                        <Title order={3}>Tutorial</Title>

                        <AspectRatio ratio={16 / 9}>
                            <iframe
                                src="https://www.youtube.com/embed/Dorf8i6lCuk"
                                title="YouTube video player"
                                frameBorder="0"
                                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                                allowFullScreen
                            />
                        </AspectRatio>
                    </>
                    </Grid.Col>
                    <Grid.Col span={8}>
                        <Stack>
                            <Card shadow="sm" padding="lg" radius="md" withBorder >
                                <Center mb={10} ><Title order={3}>Ingredients</Title></Center>
                                <List
                                    spacing="xs"
                                    size="sm"
                                    center
                                    icon={
                                        <ThemeIcon color="teal" size={24} radius="xl">
                                            <IconCircleCheck size="1rem" />
                                        </ThemeIcon>
                                    }
                                >

                                    {oatsIdliIngredients.map((ingredient) => { return (<List.Item>{ingredient}</List.Item>) })}
                                    <List.Item
                                        icon={
                                            <ThemeIcon color="red" size={24} radius="xl">
                                                <IconCircleX size="1rem" />
                                            </ThemeIcon>
                                        }
                                    >
                                        Margarine
                                    </List.Item>
                                </List>
                            </Card>
                        </Stack>
                    </Grid.Col>
                </Grid>
            </Container>
        )
    }
}

