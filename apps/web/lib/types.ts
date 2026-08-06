export type Participant = {
  id?: string;
  name: string;
  role?: string;
  aliases?: string[];
};

export type SourceLink = {
  platform?: string;
  kind?: string;
  url: string;
  preferred?: boolean;
};

export type TranscriptProvenance = {
  path: string;
  engine?: string;
  model?: string;
  selectionStatus?: string;
};

export type ShowSummary = {
  id: string;
  title: string;
  shortTitle: string;
  description: string;
  episodeCount: number;
  href: string;
  latestEpisodeHref: string;
};

export type Chapter = {
  timestamp: string;
  title: string;
  seconds: number;
  href: string;
};

export type TranscriptSegment = {
  timestamp: string;
  seconds: number;
  text: string;
  id: string;
};

export type Episode = {
  id: string;
  showId: string;
  showTitle: string;
  episodeKey: string;
  episodeNumber: number | null;
  folder: string;
  title: string;
  editorialTitle: string;
  displayTitle: string;
  subtitle: string;
  publishedAt: string;
  publishedDate: string;
  durationMs: number;
  durationLabel: string;
  participants: Participant[];
  guests: Participant[];
  hosts: Participant[];
  sources: SourceLink[];
  preferredSource?: SourceLink;
  workflow: {
    metadata?: string;
    summary?: string;
    transcript?: string;
  };
  summarySourceTranscript?: TranscriptProvenance;
  transcriptMeta: TranscriptProvenance;
  summaryRaw: string;
  transcriptRaw: string;
  readmeRaw: string;
  chapters: Chapter[];
  transcriptSegments: TranscriptSegment[];
  href: string;
};

export type EpisodeCard = Pick<
  Episode,
  | "id"
  | "showId"
  | "showTitle"
  | "episodeNumber"
  | "folder"
  | "title"
  | "editorialTitle"
  | "displayTitle"
  | "subtitle"
  | "publishedDate"
  | "durationLabel"
  | "guests"
  | "workflow"
  | "href"
>;

export type SearchResult = {
  id: string;
  title: string;
  showTitle: string;
  section: "单集" | "总结" | "逐字稿";
  snippet: string;
  href: string;
  timestamp?: string;
  score: number;
};
