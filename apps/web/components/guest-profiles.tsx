import "server-only";

import type { Participant } from "@/lib/types";

const affiliationStatusLabels = {
  current: "现任",
  former: "曾任",
} as const;

export function GuestProfiles({ guests }: { guests: Participant[] }) {
  const profiledGuests = guests.flatMap((guest) => (
    guest.profile ? [{ guest, profile: guest.profile }] : []
  ));

  if (profiledGuests.length === 0) return null;

  return (
    <section className="guest-profiles" aria-labelledby="guest-profiles-title">
      <h2 id="guest-profiles-title" className="sr-only">嘉宾背景</h2>

      <div className="guest-profiles-list">
        {profiledGuests.map(({ guest, profile }, index) => {
          const hasStructuredFacts = (
            profile.affiliations.length > 0 || profile.education.length > 0
          );
          const showHeadlineFallback = !profile.bio && !hasStructuredFacts;

          return (
            <article className="guest-profile" key={`${guest.id ?? guest.name}-${index}`}>
              <header className="guest-profile-identity">
                <h3>{guest.name}</h3>
              </header>

              <div className="guest-profile-content">
                {profile.bio ? <p className="guest-profile-bio">{profile.bio}</p> : null}
                {showHeadlineFallback ? (
                  <p className="guest-profile-bio">{profile.headline}</p>
                ) : null}

                {hasStructuredFacts ? (
                  <dl className="guest-profile-facts">
                    {profile.affiliations.length > 0 ? (
                      <div>
                        <dt>任职</dt>
                        <dd>
                          <ul>
                            {profile.affiliations.map((affiliation, affiliationIndex) => (
                              <li key={`${affiliation.organization}-${affiliation.title ?? ""}-${affiliationIndex}`}>
                                <span className="guest-profile-fact-copy">
                                  <strong>{affiliation.organization}</strong>
                                  {affiliation.title ? <span>{affiliation.title}</span> : null}
                                </span>
                                <small className="guest-profile-status">
                                  {affiliationStatusLabels[affiliation.status]}
                                </small>
                              </li>
                            ))}
                          </ul>
                        </dd>
                      </div>
                    ) : null}

                    {profile.education.length > 0 ? (
                      <div>
                        <dt>教育</dt>
                        <dd>
                          <ul>
                            {profile.education.map((education, educationIndex) => {
                              const detail = [education.credential, education.field]
                                .filter((value): value is string => Boolean(value))
                                .join(" · ");
                              return (
                                <li key={`${education.institution}-${detail}-${educationIndex}`}>
                                  <span className="guest-profile-fact-copy">
                                    <strong>{education.institution}</strong>
                                    {detail ? <span>{detail}</span> : null}
                                  </span>
                                </li>
                              );
                            })}
                          </ul>
                        </dd>
                      </div>
                    ) : null}
                  </dl>
                ) : null}
                <p className="guest-profile-checked">
                  资料核验于 <time dateTime={profile.checkedAt}>{profile.checkedAt}</time>
                  ；“现任”均指截至该日。
                </p>
              </div>
            </article>
          );
        })}
      </div>
    </section>
  );
}
