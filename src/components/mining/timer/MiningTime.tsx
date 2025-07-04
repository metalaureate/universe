import { memo } from 'react';
import { TimeSince } from '@app/utils';
import {
    MiningTimeVariant,
    MiniWrapper,
    TimerDot,
    TimerTextWrapper,
    SpacedNum,
    Wrapper,
    Heading,
    HeadingSection,
    TimerUnitWrapper,
} from './styles.ts';
import { useTranslation } from 'react-i18next';

interface MiningTimeProps {
    variant?: MiningTimeVariant;
    timing: Partial<TimeSince>;
}
export const MiningTime = memo(function MiningTime({ variant = 'primary', timing }: MiningTimeProps) {
    const { t } = useTranslation('common');
    const isMini = variant === 'mini';
    const { daysString, hoursString, minutes, seconds } = timing;

    const _minutes = isMini && minutes === '0' ? '00' : minutes;
    const _seconds = isMini && seconds === '0' ? '00' : seconds;

    const renderDays = daysString && parseInt(daysString) > 0;
    const renderHours = hoursString && parseInt(hoursString) > 0;

    const daysMarkup = renderDays ? (
        <>
            {daysString}
            <TimerUnitWrapper />
        </>
    ) : null;
    const hourMarkup = renderHours ? (
        <>
            {hoursString?.split('').map((c, i) => (
                <SpacedNum key={`hr-${i}-${c}`}>{c}</SpacedNum>
            ))}
            <TimerUnitWrapper $variant={variant}>{isMini ? ':' : `h`}</TimerUnitWrapper>
        </>
    ) : null;

    const minuteMarkup = (
        <>
            {_minutes?.split('').map((c, i) => (
                <SpacedNum key={`min-${i}-${c}`}>{c}</SpacedNum>
            ))}
            <TimerUnitWrapper $variant={variant}>{isMini ? ':' : `m`}</TimerUnitWrapper>
        </>
    );
    const secondMarkup = (
        <>
            {_seconds?.split('').map((c, i) => (
                <SpacedNum key={`sec-${i}-${c}`}>{c}</SpacedNum>
            ))}
            <TimerUnitWrapper $variant={variant}>{!isMini && 's'}</TimerUnitWrapper>
        </>
    );

    // TODO: dedupe from block time/make reusable spaced counter?

    const markup = (
        <TimerTextWrapper $variant={variant}>
            {daysMarkup}
            {hourMarkup}
            {minuteMarkup}
            {secondMarkup}
        </TimerTextWrapper>
    );

    if (!minutes && !renderHours && (!seconds || parseInt(seconds) === 0)) return null;
    if (variant === 'mini') {
        return (
            <MiniWrapper>
                <TimerDot />
                {markup}
            </MiniWrapper>
        );
    }
    return (
        <Wrapper>
            <HeadingSection>
                <Heading>{t('time-mining')}</Heading>
                <TimerDot />
            </HeadingSection>
            {markup}
        </Wrapper>
    );
});
