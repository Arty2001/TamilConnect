import { IconBookmark, IconHeart, IconShare } from "@tabler/icons-react";
import { Card, Image, Text, Group, createStyles, rem } from "@mantine/core";

const useStyles = createStyles((theme) => ({
  card: {
    position: "relative",
    backgroundColor:
      theme.colorScheme === "dark" ? theme.colors.dark[7] : theme.white,
  },

  rating: {
    position: "absolute",
    top: theme.spacing.xs,
    right: rem(12),
    pointerEvents: "none",
  },

  title: {
    display: "block",
    marginTop: theme.spacing.md,
    marginBottom: rem(5),
  },

  action: {
    backgroundColor:
      theme.colorScheme === "dark"
        ? theme.colors.dark[6]
        : theme.colors.gray[0],
    ...theme.fn.hover({
      backgroundColor:
        theme.colorScheme === "dark"
          ? theme.colors.dark[5]
          : theme.colors.gray[1],
    }),
  },

  footer: {
    marginTop: theme.spacing.md,
  },
}));

interface ArticleCardProps {
  image: string;
  title: string;
}

function ArticleCard({
  className,
  image,
  title,
  ...others
}: ArticleCardProps &
  Omit<React.ComponentPropsWithoutRef<"div">, keyof ArticleCardProps>) {
  const { classes, cx, theme } = useStyles();
  const linkProps = {
    //href: link,
    target: "_blank",
    rel: "noopener noreferrer",
  };

  return (
    <Card
      withBorder
      radius="md"
      className={cx(classes.card, className)}
      {...others}
    >
      <Card.Section>
        <a {...linkProps}>
          <Image src={image} height={180} />
        </a>
      </Card.Section>

      <Text className={classes.title} fw={500} component="a" {...linkProps}>
        {title}
      </Text>

      <Group position="apart" className={classes.footer}></Group>
    </Card>
  );
}

export function ArticleCards() {
  return ArticleCard({
    className: "card1",
    image:
      "https://th-thumbnailer.cdn-si-edu.com/qwdFU8TzPixEtFzRLC2V_Ezr2tw=/fit-in/1600x0/https%3A%2F%2Ftf-cmsv2-smithsonianmag-media.s3.amazonaws.com%2Ffiler%2Fd5%2F24%2Fd5243019-e0fc-4b3c-8cdb-48e22f38bff2%2Fistock-183380744.jpg",
    title: "banana",
  });
}
