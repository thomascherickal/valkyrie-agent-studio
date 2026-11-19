import { fireEvent, render, screen, waitFor, within } from "@testing-library/react";
import { afterEach, beforeAll, describe, expect, it, vi } from "vitest";
import { App } from "../App";
import { ThemeProvider } from "../theme/ThemeProvider";
import { appRoutes, originalOf, polyfillDialog, stubFetch } from "./helpers";

beforeAll(polyfillDialog);
afterEach(() => vi.unstubAllGlobals());

const PRD = originalOf("01-product-management", "01-prd-architect");
const source = () => screen.getByLabelText("Python Source") as HTMLTextAreaElement;
const tab = (name: string) => fireEvent.click(screen.getByText(name, { selector: "[role=tab]" }));
const edit = (v: string) => fireEvent.change(source(), { target: { value: v } });
const click = (name: string) => fireEvent.click(screen.getByRole("button", { name }));
const problems = () => within(screen.getByRole("region", { name: "Problems" }));
const heading = () => problems().getByRole("heading").textContent;

describe("App Problems list", () => {
  it("receives errors from a failed Save, a failed Check and a failed Run, newest first, and clears", async () => {
    stubFetch(appRoutes);
    render(<ThemeProvider><App /></ThemeProvider>);
    expect(problems().getByText("No errors from checking, saving or running.")).toBeTruthy();
    fireEvent.change(screen.getByLabelText("Experience Mode"), { target: { value: "advanced" } });
    tab("Python");
    await waitFor(() => expect(source().value).toBe(PRD));

    edit("FAIL");
    click("Save changes");
    await waitFor(() => expect(heading()).toBe("Problems 1"));
    expect(problems().getByRole("alert").textContent).toContain("save · PRD Architect · rules");
    expect(problems().getByRole("alert").textContent).toContain("Code is not allowed");

    edit("BOOM");
    click("Check for errors");
    await waitFor(() => expect(heading()).toBe("Problems 2"));
    expect(problems().getAllByRole("alert")[0].textContent).toContain("check · PRD Architect · rules");
    expect(problems().getAllByRole("alert")[0].textContent).toContain("BOOM happened");

    tab("Run");
    fireEvent.change(screen.getByLabelText("Feature brief"), { target: { value: "BOOM" } });
    click("Run agent");
    await waitFor(() => expect(heading()).toBe("Problems 3"));
    const items = problems().getAllByRole("alert").map((li) => li.textContent!);
    expect(items[0]).toContain("run · PRD Architect · model");
    expect(items[0]).toContain("Run blew up");
    expect(items[1]).toContain("check");
    expect(items[2]).toContain("save");

    click("Clear problems");
    expect(heading()).toBe("Problems 0");
    expect(problems().getByText("No errors from checking, saving or running.")).toBeTruthy();
  });
  it("a failed run of an implementation names it", async () => {
    stubFetch(appRoutes);
    render(<ThemeProvider><App /></ThemeProvider>);
    await screen.findByRole("option", { name: "Python: Hybrid" });
    fireEvent.change(screen.getByLabelText("Run with"), { target: { value: "hybrid" } });
    fireEvent.change(screen.getByLabelText("Feature brief"), { target: { value: "BOOM" } });
    click("Run agent");
    await waitFor(() => expect(heading()).toBe("Problems 1"));
    expect(problems().getByRole("alert").textContent).toContain("run · PRD Architect · hybrid");
  });
});
