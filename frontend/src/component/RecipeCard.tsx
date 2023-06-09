import { IconBookmark, IconHeart, IconShare } from '@tabler/icons-react';
import {
    Card,
    Image,
    Text,
    ActionIcon,
    Badge,
    Group,
    Center,
    Avatar,
    createStyles,
    rem,
} from '@mantine/core';

const useStyles = createStyles((theme) => ({
    card: {
        position: 'relative',
        backgroundColor: theme.colorScheme === 'dark' ? theme.colors.dark[7] : theme.white,
        width: 300
    },

    rating: {
        position: 'absolute',
        top: theme.spacing.xs,
        right: rem(12),
        pointerEvents: 'none',
    },

    title: {
        display: 'block',
        marginTop: theme.spacing.md,
        marginBottom: rem(5),
    },

    action: {
        backgroundColor: theme.colorScheme === 'dark' ? theme.colors.dark[6] : theme.colors.gray[0],
        ...theme.fn.hover({
            backgroundColor: theme.colorScheme === 'dark' ? theme.colors.dark[5] : theme.colors.gray[1],
        }),
    },

    footer: {
        marginTop: theme.spacing.md,
    },
}));

interface RecipeCardProps {
    image: string;
    title: string;
    description: string;
    rating: string;
    author: {
        name: string;
        image: string;
    };
}

export function RecipeCard({
    className,
    image,
    title,
    description,
    author,
    rating,
    ...others
}: RecipeCardProps & Omit<React.ComponentPropsWithoutRef<'div'>, keyof RecipeCardProps>) {
    const { classes, cx, theme } = useStyles();

    return (
        <Card withBorder radius="md" className={cx(classes.card, className)} {...others}>
            <Card.Section>
                <Image src={image} height={180} />
            </Card.Section>

            <Badge className={classes.rating} variant="gradient" gradient={{ from: 'yellow', to: 'red' }}>
                {rating}
            </Badge>

            <Text className={classes.title} fw={500} component="a">
                {title}
            </Text>

            <Text fz="sm" color="dimmed" lineClamp={4}>
                {description}
            </Text>

            <Group position="apart" className={classes.footer}>
                <Center>
                    <Avatar src={author.image} size={24} radius="xl" mr="xs" />
                    <Text fz="sm" inline>
                        {author.name}
                    </Text>
                </Center>

                <Group spacing={8} mr={0}>
                    <ActionIcon className={classes.action}>
                        <IconHeart size="1rem" color={theme.colors.red[6]} />
                    </ActionIcon>
                    <ActionIcon className={classes.action}>
                        <IconShare size="1rem" />
                    </ActionIcon>
                </Group>
            </Group>
        </Card>
    );
}