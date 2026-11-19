import { fireEvent, render, screen } from "@testing-library/react";
import { beforeAll, describe, expect, it, vi } from "vitest";
import { DeployDialog } from "../components/DeployDialog";
import { deployed, polyfillDialog } from "./helpers";

beforeAll(polyfillDialog);

describe("DeployDialog", () => {
  it("opens through states and closes", () => {
    const onClose = vi.fn();
    const { container, rerender } = render(<DeployDialog state={{ kind: "idle" }} onClose={onClose} />);
    const dialog = container.querySelector("dialog")!;
    expect(dialog.open).toBe(false);
    rerender(<DeployDialog state={{ kind: "loading" }} onClose={onClose} />);
    expect(dialog.open).toBe(true);
    expect(screen.getByText("Deploy to Rust")).toBeTruthy();
    rerender(<DeployDialog state={{ kind: "done", data: deployed }} onClose={onClose} />);
    expect(dialog.open).toBe(true);
    expect(screen.getByText("Deployed to Rust: crate-x")).toBeTruthy();
    expect(screen.getByText("Benchmark: 10x")).toBeTruthy();
    expect(screen.getByText(/does not include Python you wrote or edited/)).toBeTruthy();
    expect(screen.getByLabelText("main.rs").textContent).toBe("fn main(){}");
    fireEvent.click(screen.getByText("Close"));
    fireEvent(dialog, new Event("cancel"));
    expect(onClose).toHaveBeenCalledTimes(2);
    rerender(<DeployDialog state={{ kind: "error", message: "bad" }} onClose={onClose} />);
    expect(screen.getByRole("alert").textContent).toBe("bad");
    rerender(<DeployDialog state={{ kind: "idle" }} onClose={onClose} />);
    expect(dialog.open).toBe(false);
  });
});
