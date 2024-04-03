import { PropsWithChildren, FC } from "react";

import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import Button from "@mui/material/Button";
import { Link } from "react-router-dom";

const BaseLayout: FC<PropsWithChildren> = ({ children }) => {
  const isWordsOpened = window.location.pathname === "/words";

  return (
    <Box>
      <AppBar position="static">
        <Container maxWidth="xl">
          <Toolbar disableGutters>
            <Typography
              variant="h6"
              noWrap
              component="a"
              href="/"
              sx={{
                mr: 2,
                display: { xs: "none", md: "flex" },
                fontFamily: "monospace",
                fontWeight: 700,
                color: "inherit",
                textDecoration: "none",
              }}
            >
              Pocketbook Dictionary
            </Typography>
            
            <Box sx={{ flexGrow: 1, display: { xs: "none", md: "flex" } }}>
              <Button
                key={"Books"}
                sx={{ my: 2, color: "white", display: "block" }}
                component={Link}
                to={"/books"}
              >
                Books
              </Button>
              <Button
                key={"Words"}
                sx={{ my: 2, color: "white", display: "block" }}
                component={Link}
                to={"/words"}
              >
                Words
              </Button>
            </Box>
          </Toolbar>
        </Container>
      </AppBar>
      <Box>{children}</Box>
    </Box>
  );
};

export default BaseLayout;
