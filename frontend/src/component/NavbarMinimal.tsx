import { Navbar, Center, Tooltip, UnstyledButton, createStyles, Stack, rem } from '@mantine/core';
import {
    IconFridge,
    IconGauge,
    IconDeviceDesktopAnalytics,
    IconLogout,
    IconSwitchHorizontal,
} from '@tabler/icons-react';
import { MantineLogo } from '@mantine/ds';
import { useNavigate , useLocation } from "react-router-dom";

const useStyles = createStyles((theme) => ({
    link: {
        width: rem(50),
        height: rem(50),
        borderRadius: theme.radius.md,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        color: theme.colorScheme === 'dark' ? theme.colors.dark[0] : theme.colors.gray[7],

        '&:hover': {
            backgroundColor: theme.colorScheme === 'dark' ? theme.colors.dark[5] : theme.colors.gray[0],
        },
    },

    active: {
        '&, &:hover': {
            backgroundColor: theme.fn.variant({ variant: 'light', color: theme.primaryColor }).background,
            color: theme.fn.variant({ variant: 'light', color: theme.primaryColor }).color,
        },
    },
}));

interface NavbarLinkProps {
    icon: React.FC<any>;
    label: string;
    active?: boolean;
    onClick?(): void;
}

function NavbarLink({ icon: Icon, label, active, onClick }: NavbarLinkProps) {
    const { classes, cx } = useStyles();
    return (
        <Tooltip label={label} position="right" transitionProps={{ duration: 0 }}>
            <UnstyledButton onClick={onClick} className={cx(classes.link, { [classes.active]: active })}>
                <Icon size="1.2rem" stroke={1.5} />
            </UnstyledButton>
        </Tooltip>
    );
}

const mockdata = [
    { icon: IconFridge, label: 'Home' },
    { icon: IconGauge, label: 'FindPage' },
    { icon: IconDeviceDesktopAnalytics, label: 'SearchPage' }
];

export function NavbarMinimal() {

    let navigate = useNavigate();
    const routeChange = (label:any) => {
        navigate(label);
    } 

    const location = useLocation();

    console.log(location.pathname)

    const links = mockdata.map((link, index) => (
        <NavbarLink
            {...link}
            key={link.label}
            active={location.pathname==="/"+link.label}
            onClick={() => routeChange(link.label)}
        />
    ));

    return (
        <Navbar width={{ base: 80 }} p="md">
            <Center>
                <MantineLogo type="mark" size={30} />
            </Center>
            <Navbar.Section grow mt={50}>
                <Stack justify="center" spacing={0}>
                    {links}
                </Stack>
            </Navbar.Section>
            <Navbar.Section>
                <Stack justify="center" spacing={0}>
                    <NavbarLink icon={IconSwitchHorizontal} label="Change account" />
                    <NavbarLink icon={IconLogout} label="Logout" />
                </Stack>
            </Navbar.Section>
        </Navbar>
    );
}