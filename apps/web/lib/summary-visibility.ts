const hiddenFactBoundaryHeading = /^##\s+(?:事实边界与待核实(?:事项)?|证据、推断与人工(?:审核|复核)边界)\s*$/mu;

export function getWebVisibleSummaryMarkdown(markdown: string): string {
  const headingMatch = hiddenFactBoundaryHeading.exec(markdown);
  if (!headingMatch) return markdown;

  const sectionStart = headingMatch.index;
  const remainderStart = headingMatch.index + headingMatch[0].length;
  const remainder = markdown.slice(remainderStart);
  const nextHeading = /^##\s+/mu.exec(remainder);
  const sectionEnd = nextHeading
    ? remainderStart + nextHeading.index
    : markdown.length;

  const before = markdown.slice(0, sectionStart).trimEnd();
  const after = markdown.slice(sectionEnd).trimStart();
  return after ? `${before}\n\n${after}` : before;
}
