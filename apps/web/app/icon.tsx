import { ImageResponse } from "next/og";

export const size = {
  width: 64,
  height: 64,
};

export const contentType = "image/png";

export default function Icon() {
  return new ImageResponse(
    (
      <div
        style={{
          width: "100%",
          height: "100%",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          color: "#fbfaf6",
          background: "#e83a2a",
          borderRadius: 14,
          fontFamily: "serif",
          fontSize: 46,
          fontWeight: 700,
          letterSpacing: "-0.08em",
          paddingRight: 3,
        }}
      >
        P
      </div>
    ),
    size,
  );
}
