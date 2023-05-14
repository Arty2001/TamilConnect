import { createStyles, Container, Text, rem, Box } from "@mantine/core";
import { GithubIcon } from "@mantine/ds";

const useStyles = createStyles((theme) => ({
  wrapper: {
    position: "relative",
    boxSizing: "content-box",
    backgroundColor:
      theme.colorScheme === "dark" ? theme.colors.dark[8] : theme.white,

    display: "flex",
    alignItems: "center",
    marginTop: "1px",
    width: "100%",
  },

  inner: {
    position: "relative",
    paddingTop: rem(0),
    paddingBottom: rem(0),

    [theme.fn.smallerThan("sm")]: {
      paddingBottom: rem(80),
      paddingTop: rem(80),
    },
  },

  title: {
    fontFamily: `Greycliff CF, ${theme.fontFamily}`,
    fontSize: rem(62),
    fontWeight: 900,
    lineHeight: 1.1,
    margin: 0,
    padding: 0,
    color: theme.colorScheme === "dark" ? theme.white : theme.black,

    [theme.fn.smallerThan("sm")]: {
      fontSize: rem(42),
      lineHeight: 1.2,
    },
  },

  description: {
    marginTop: theme.spacing.xl,
    fontSize: rem(24),

    [theme.fn.smallerThan("sm")]: {
      fontSize: rem(18),
    },
  },
}));

export function HeroTitle() {
  const { classes } = useStyles();

  return (
    <div className={classes.wrapper}>
      <Box
        sx={(theme) => ({
          backgroundColor:
            theme.colorScheme === "dark"
              ? theme.colors.dark[6]
              : theme.colors.blue[0],
          textAlign: "center",
          padding: theme.spacing.xl,
          borderRadius: theme.radius.md,
        })}
      >
        <Container size={700} className={classes.inner}>
          <h1 className={classes.title}>
            {" "}
            <Text
              component="span"
              variant="gradient"
              gradient={{ from: "blue", to: "cyan" }}
              inherit
            >
              Welcome Back!
            </Text>{" "}
          </h1>

          <Text className={classes.description} color="dimmed">
            The dashboard page allows you to discover trending recipies and add
            groceries to your cart.
          </Text>
        </Container>
      </Box>
    </div>
  );
}
